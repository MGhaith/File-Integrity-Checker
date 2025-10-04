#!/usr/bin/env python3
import os
import sys
import hashlib
import json
from pathlib import Path

HASH_STORE = Path.home() / ".integrity_hashes.json"

def compute_hash(file_path):
    """Compute SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def load_hashes():
    if HASH_STORE.exists():
        with open(HASH_STORE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_STORE, "w") as f:
        json.dump(hashes, f, indent=4)

def init(path):
    hashes = {}
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                hashes[file_path] = compute_hash(file_path)
    else:
        hashes[path] = compute_hash(path)
    save_hashes(hashes)
    print("Hashes stored successfully.")

def check(path):
    hashes = load_hashes()
    if not hashes:
        print("No hashes stored. Run 'init' first.")
        return
    files_to_check = []
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                files_to_check.append(os.path.join(root, file))
    else:
        files_to_check.append(path)

    for file in files_to_check:
        new_hash = compute_hash(file)
        old_hash = hashes.get(file)
        if not old_hash:
            print(f"{file}: New file (not in baseline)")
        elif new_hash != old_hash:
            print(f"{file}: Modified (Hash mismatch)")
        else:
            print(f"{file}: Unmodified")

def usage(bool=True):
    if bool:
        print("Usage: ./integrity-check [init|check|update] <file_or_dir>")
    else:
        print("Usage: [init|check|update] <file_or_dir>")

def interactive_loop():
    while True:
        user_input = input("Enter command and path (or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            break
        parts = user_input.split(maxsplit=1)
        if len(parts) != 2:
            usage(False)
            continue
        cmd, tgt = parts
        if cmd in {"init", "check", "update"}:
            globals()[cmd](tgt)
        else:
            print("Invalid command. Use init, check, or update.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        input("Press a button to exit...")
        sys.exit(1)

    command, target = sys.argv[1], sys.argv[2]
    if command in {"init", "check", "update"}:
        globals()[command](target)
    else:
        print("Invalid command. Use init, check, or update.")
        interactive_loop()

#!/usr/bin/env python3
import os
import sys
import hashlib
import json
from pathlib import Path

HASH_STORE = Path.home() / ".integrity_hashes.json"

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

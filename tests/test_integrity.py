import os
import tempfile
from integrity_check import compute_hash, init, check, update, load_hashes
from integrity_checker.integrity_check import compute_hash, init, check, update, load_hashes

def test_hash_computation():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"hello world")
        tmp_path = tmp.name
    hash1 = compute_hash(tmp_path)
    with open(tmp_path, "a") as f:
        f.write("!")
    hash2 = compute_hash(tmp_path)
    os.remove(tmp_path)
    assert hash1 != hash2

def test_init_and_check():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
        tmp.write("log entry")
        tmp_path = tmp.name
    init(tmp_path)
    hashes = load_hashes()
    assert tmp_path in hashes
    os.remove(tmp_path)

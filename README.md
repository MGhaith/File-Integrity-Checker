# File Integrity Checker (WiP)
A simple tool to verify the integrity of log files using SHA-256 hashes.  
Helps detect tampering or unauthorized modifications to system/application logs.

## Setup

1. Clone the repo:
    ```bash
    git clone https://github.com/MGhaith/File-Integrity-Checker.git
    cd File-Integrity-Checker/integrity_checker
    chmod +x integrity-check.py # for linux
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Usage

- Initialize the checker with a directory or file path to monitor.
    ```bash
    ./integrity_check.py init <file_or_dir>
    ```
- Run the checker periodically to verify log file integrity.
    ```bash
    ./integrity_check.py check <file_or_dir>
    ```
- Update the hashes for monitored files/directories.
    ```bash
    ./integrity_check.py update <file_or_dir>
    ```
- Check the output for any changes detected.

### Example
```bash
> ./integrity-check init /var/log  # Initializes and stores hashes of all log files in the directory
> Hashes stored successfully.

> ./integrity-check check /var/log/syslog
> Status: Modified (Hash mismatch)

> ./integrity-check -check /var/log/auth.log
> Status: Unmodified

> ./integrity-check update /var/log/syslog
> Hash updated successfully.

```	

## Testing
Unit tests are provided in `test_integrity.py` and cover the core functionalities:

- `test_hash_computation`: Verifies that changing a file alters its SHA-256 hash.
- `test_init_and_check`: Ensures that `init` stores hashes and `check` can later verify them.

Run the full test suite from the repository root (`File-Integrity-Checker`):
```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/MGhaith/File-Integrity-Checker/blob/main/LICENSE) file for details.
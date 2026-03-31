# Auto IT Support Toolkit
 Automated IT support toolkit for real-time system monitoring, issue detection, remediation, and ticket generation.

 ---

## Features
- **System Monitoring**
    - CPU, memory, and disk usage tracking
    - Active process monitoring

- **Issue Detection**
    - Detects high CPU, memory, and disk usage
    - Identifies missing critical system processes

- **Severity Classification**
    - Issues categorized as:
        - LOW
        - MEDIUM
        - HIGH
        - CRITICAL

- **Automated Remediation**
    - Clears temporary files for disk issues
    - Attempts service recovery (platform-dependent)
    - Escelates unsafe scenarios to manual intervention

- **Logging**
    - Timestamped logs with severity levels

- **Ticket Generation**
    - Structured JSON tickets for each detected issue
    - Includes severity, action taken, and status

- **Safety Controls**
    - Limits automated fixes to **3 attempts per issue type**
    - Prevents infinite loops and excessive system modification

---

## Cross-Platform Support

This tool automatically adapts behavior based on the operating system:

### Windows
- Uses `C:/` for disk monitoring
- Cleans `%TEMP%` directory
- Monitors critical system process: `svchost`
- Simulates safe service handling (no unsafe system manipulation)

### Linux / macOS
- Uses `/` for disk monitoring
- Cleans `/tmp` directory
- Monitors critical service: `ssh`
- Attempts service restart using system-level commands (Linux)

---

## Installation

```bash
pip install -r requirements.txt
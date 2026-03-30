# auto-it-support-toolkit
Automated IT support toolkit: system monitoring, issue detection, and ticketing

## Features
- System monitoring (CPU, memory, disk)
- Issue detection
- Automated fixes
- Logging
- Ticket generation

## Run
pip install -r requirements.txt
python main.py

## Cross-Platform Support
This tool automatically adapts behavior based on the operating system:
- Windows: Uses native temp cleanup and simulated service handling
- Linux/macOS: Uses system-level commands and real service checks

## Safety Features
- Limits automated fixes to 3 attempts per issue
- Prevents infinite loops and excessive system modification
- Designed to simulate real-world IT support workflows safely
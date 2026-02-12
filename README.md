# Security Log Analyzer (Brute-Force Detection) testing tetsgi

# Overview
This project is a Python-based security log analyzer designed to simulate basic SOC (Security Operations Center) detection logic. It parses Linux authentication logs to identify potential brute-force login attempts and assigns severity levels based on configurable thresholds. 

# Features
- Parses Linux `auth.log` files
- Detects failed SSH login attempts
- Applies severity classification:
  - **LOW**: 1–2 failed attempts
  - **MEDIUM**: 3–4 failed attempts
  - **HIGH**: 5+ failed attempts
- Outputs SOC-style alert messages

# Example Output
```text
Security Alert Report:
[INFO]  10.0.0.5 | Attempts: 1 | Severity: LOW
[ALERT] 192.168.1.10 | Attempts: 3 | Severity: MEDIUM
[ALERT] 198.51.100.22 | Attempts: 5 | Severity: HIGH

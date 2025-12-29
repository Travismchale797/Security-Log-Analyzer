from collections import defaultdict
import sys

def parse_auth_log(file_path):
    failed_logins = defaultdict(int)

    with open(file_path, "r") as file:
        for line in file:
            if "Failed password" in line:
                parts = line.split()
                ip = parts[-4]
                failed_logins[ip] += 1

    return failed_logins

def get_severity(count):
    if count >= 5:
        return "HIGH"
    elif count >= 3:
        return "MEDIUM"
    else:
        return "LOW"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 log_analyzer.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]
    results = parse_auth_log(log_file)

    print("\nSecurity Alert Report:")
    for ip, count in results.items():
        severity = get_severity(count)

        if count > 3:
            print(f"[ALERT] {ip} | Attempts: {count} | Severity: {severity}")
        else:
            print(f"[INFO]  {ip} | Attempts: {count} | Severity: {severity}")


if __name__ == "__main__":
    main()

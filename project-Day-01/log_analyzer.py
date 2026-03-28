from datetime import datetime
from collections import Counter

LOG_FILE = "app.log"
REPORT_FILE = "report.txt"

def analyze_logs(file_path):
    counts = Counter({"INFO": 0, "WARNING": 0, "ERROR": 0})
    error_lines = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()

                if "ERROR" in line:
                    counts["ERROR"] += 1
                    error_lines.append(line)

                elif "WARNING" in line:
                    counts["WARNING"] += 1

                elif "INFO" in line:
                    counts["INFO"] += 1

    except FileNotFoundError:
        print("❌ Log file not found!")
        return None, None

    return counts, error_lines


def generate_report(counts, error_lines):
    print("\n📊 ----- Log Analysis Report -----")
    print(f"INFO    : {counts['INFO']}")
    print(f"WARNING : {counts['WARNING']}")
    print(f"ERROR   : {counts['ERROR']}")

    with open(REPORT_FILE, "w") as report:
        report.write(f"Report Generated At: {datetime.now()}\n\n")
        report.write(f"INFO    : {counts['INFO']}\n")
        report.write(f"WARNING : {counts['WARNING']}\n")
        report.write(f"ERROR   : {counts['ERROR']}\n\n")

        if error_lines:
            report.write("Error Details:\n")
            for err in error_lines:
                report.write(err + "\n")

    print("\n✅ Report saved in report.txt")


def main():
    counts, error_lines = analyze_logs(LOG_FILE)

    if counts:
        generate_report(counts, error_lines)


if __name__ == "__main__":
    main()

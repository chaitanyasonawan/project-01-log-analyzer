# Simple Log Analyzer Tool
# Counts INFO, WARNING, ERROR messages from a log file

log_file = "app.log"
report_file = "report.txt"

# Initialize counters
info_count = 0
warning_count = 0
error_count = 0

# Read the log file
with open(log_file, "r") as file:
    for line in file:
        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "ERROR" in line:
            error_count += 1

# Print results
print(f"INFO : {info_count}")
print(f"WARNING : {warning_count}")
print(f"ERROR : {error_count}")

# Write report to file
with open(report_file, "w") as report:
    report.write(f"INFO : {info_count}\n")
    report.write(f"WARNING : {warning_count}\n")
    report.write(f"ERROR : {error_count}\n")

print(f"\nReport saved to {report_file}")

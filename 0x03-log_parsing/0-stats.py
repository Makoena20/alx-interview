#!/usr/bin/python3
import sys
import re
from collections import defaultdict

def print_stats(file_size, status_counts):
    print(f"File size: {file_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")

def parse_line(line):
    match = re.match(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$', line)
    if match:
        status_code, file_size = match.group(2), int(match.group(3))
        return status_code, file_size
    return None, None

def main():
    file_size = 0
    status_counts = defaultdict(int)
    lines_processed = 0

    try:
        for line in sys.stdin:
            status_code, size = parse_line(line)
            if status_code and size is not None:
                file_size += size
                status_counts[status_code] += 1
                lines_processed += 1

                if lines_processed % 10 == 0:
                    print_stats(file_size, status_counts)
    except KeyboardInterrupt:
        print_stats(file_size, status_counts)

if __name__ == "__main__":
    main()


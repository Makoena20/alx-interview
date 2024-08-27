#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

# Initialize counters and accumulators
status_codes = defaultdict(int)
total_file_size = 0
line_count = 0

def print_stats():
    """Prints the accumulated statistics."""
    global total_file_size, status_codes
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL+C)."""
    print_stats()
    sys.exit(0)

def main():
    global total_file_size, status_codes, line_count
    
    # Register signal handler for keyboard interruption
    signal.signal(signal.SIGINT, signal_handler)
    
    for line in sys.stdin:
        parts = line.split()
        if len(parts) == 7 and parts[2] == '-' and parts[3].startswith('[') and parts[4].startswith('"GET') and parts[5].startswith('HTTP') and parts[6].isdigit():
            try:
                # Extract file size and status code
                file_size = int(parts[6])
                status_code = int(parts[5].split('/')[1])
                
                # Update counters
                total_file_size += file_size
                status_codes[status_code] += 1
                line_count += 1
                
                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats()
                    # Reset counters for the next batch
                    total_file_size = 0
                    status_codes = defaultdict(int)
                    
    # Print final stats if no interruption occurred
    print_stats()

if __name__ == "__main__":
    main()


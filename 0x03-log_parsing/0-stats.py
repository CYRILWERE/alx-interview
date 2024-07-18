#!/usr/bin/python3
import sys
import re

def print_stats(total_size, status_codes):
    """Prints the accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def main():
    total_size = 0
    line_count = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    
    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>.+)\] "GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)'
    )
    
    try:
        for line in sys.stdin:
            match = log_pattern.match(line)
            if match:
                size = int(match.group('size'))
                status = int(match.group('status'))
                
                total_size += size
                if status in status_codes:
                    status_codes[status] += 1
                
                line_count += 1
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()


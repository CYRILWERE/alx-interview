#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

def generate_log_line():
    """Generates a single log line in the specified format."""
    ip = "{:d}.{:d}.{:d}.{:d}".format(random.randint(1, 255), random.randint(1, 255),
                                      random.randint(1, 255), random.randint(1, 255))
    date = datetime.datetime.now().strftime('%d/%b/%Y:%H:%M:%S %z')
    status = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    size = random.randint(1, 1024)
    log_line = '{} - [{}] "GET /projects/260 HTTP/1.1" {} {}\n'.format(ip, date, status, size)
    return log_line

if __name__ == "__main__":
    for _ in range(10000):
        sleep(random.random())
        sys.stdout.write(generate_log_line())
        sys.stdout.flush()


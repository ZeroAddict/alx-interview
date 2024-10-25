#!/usr/bin/python3

import sys
import re

# Constants
PRINT_INTERVAL = 10
STATUS_CODES = ['200', '301', '400', '401', '403', '404', '405', '500']

# Initialize metrics
file_size = 0
status_code_counts = {code: 0 for code in STATUS_CODES}

def extract_input(input_line):
    pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_fmt = '{}\-{}{}{}{}\s*'.format(pattern[0], pattern[1], pattern[2], pattern[3], pattern[4])
    resp_match = re.fullmatch(log_fmt, input_line)

    info = {
        'status_code': 0,
        'file_size': 0,
    }

    if resp_match:
        info['status_code'] = resp_match.group('status_code')
        info['file_size'] = int(resp_match.group('file_size'))

    return info

def update_metrics(info):
    global file_size
    global status_code_counts

    file_size += info['file_size']
    status_code = info['status_code']

    if status_code in STATUS_CODES:
        status_code_counts[status_code] += 1

def print_log_parser():
    print("File size: {}".format(file_size))
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))

def run():
    count = 0

    for line in sys.stdin:
        line = line.strip()
        info = extract_input(line)

        if info['status_code'] and info['file_size']:
            update_metrics(info)
            count += 1

            if count % PRINT_INTERVAL == 0:
                print_log_parser()

    print_log_parser()

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print_log_parser()
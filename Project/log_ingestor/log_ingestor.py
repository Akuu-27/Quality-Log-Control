# log_ingestor.py

import os
from log_format import format_log

def write_log(log, log_file):
    with open(log_file, 'a') as f:
        f.write(log + '\n')

def log_api_event(level, log_string, source):
    log = format_log(level, log_string, source)
    log_file = f"{source}.log"
    write_log(log, log_file)

# Example usage:
log_api_event("error", "Failed to connect to database", "api1")
log_api_event("info", "Request received", "api2")

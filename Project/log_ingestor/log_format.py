# log_format.py

import json
from datetime import datetime

def format_log(level, log_string, source):
    timestamp = datetime.utcnow().isoformat() + 'Z'
    log = {
        "level": level,
        "log_string": log_string,
        "timestamp": timestamp,
        "metadata": {
            "source": source
        }
    }
    return json.dumps(log)

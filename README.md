# Quality-Log-Control

Overview
This project aims to develop a Log Control System consisting of two main components: the Log Ingestor and the Query Interface. The Log Ingestor captures logs from different stages via APIs and stores them in designated log files, while the Query Interface provides users with a convenient way to search and filter through the collected log data.

Features
Log Ingestor:

Integrates with multiple APIs to capture logs.
Standardizes log format and stores logs in designated log files.
Allows configuration of logging levels and file paths.
Implements robust error handling mechanisms.
Query Interface:

Provides a user-friendly interface (CLI) for searching logs.
Offers filtering options based on log level, log message, timestamp, and source.
Supports efficient full-text search across logs.
Implements advanced features such as date range search and regular expressions (bonus).

Directory Structure
project_directory/
│
├── log_ingestor/
│   ├── log_format.py
│   ├── log_ingestor.py
│   └── config.json
│
└── query_interface/
    └── query_interface.py

Setup and Usage
Clone the Repository:
git clone https://github.com/your-username/log-control-system.git
cd log-control-system

Install Dependencies:
pip install -r requirements.txt

Run Log Ingestor:
python log_ingestor/log_ingestor.py

Run Query Interface:
python query_interface/query_interface.py --level error

Sample Queries
Find all logs with the level set to "error".
Search for logs with the message containing the term "Failed to connect".
Filter logs between the timestamp "2023-09-10T00:00:00Z" and "2023-09-15T23:59:59Z".

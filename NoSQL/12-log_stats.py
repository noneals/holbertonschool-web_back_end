#!/usr/bin/env python3
"""Print Nginx log statistics stored in MongoDB."""
from pymongo import MongoClient


def log_stats() -> None:
    """Display total logs, per-method counts, and GET /status count."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db_nginx = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    count_logs = db_nginx.count_documents({})
    print(f'{count_logs} logs')

    print('Methods:')
    for method in methods:
        count_method = db_nginx.count_documents({'method': method})
        print(f'\tmethod {method}: {count_method}')

    check = db_nginx.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{check} status check')


if __name__ == "__main__":
    log_stats()

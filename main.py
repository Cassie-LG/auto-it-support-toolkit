import json
import time
from monitor import get_system_stats
from detector import detect_issues
from fixer import fix_issue
from logger import log_event
from ticket import create_ticket

#Load config
with open("config.json") as f:
    config = json.load(f)

#Main loop
while True:
    stats = get_system_stats()
    issues = detect_issues(stats, config)

    for issue in issues:
        log_event(issue["message"])
        action = fix_issue(issue)
        create_ticket(issue, action)
        print(f"[ISSUE] {issue['message']} -> {action}")
    
    time.sleep(config["check_interval"])
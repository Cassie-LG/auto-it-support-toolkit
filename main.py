import json
import time
from monitor import get_system_stats
from detector import detect_issues
from fixer import fix_issue
from logger import log_event
from ticket import create_ticket

#Track number of fix attempts per issue type
attempts = {}
MAX_ATTEMPTS = 3

#Load config
with open("config.json") as f:
    config = json.load(f)

#Main loop
while True:
    stats = get_system_stats()
    issues = detect_issues(stats, config)

    for issue in issues:
        issue_type = issue["type"]
        severity = issue["severity"]

        #Initialize counter
        if issue_type not in attempts:
            attempts[issue_type] = 0

        log_event(issue["message"], severity)

        #Only attempt to fix up to MAX_ATTEMPTS
        if attempts[issue_type] < MAX_ATTEMPTS:
            action = fix_issue(issue)
            attempts[issue_type] += 1
        else:
            action = "Max fix attempts reached"
            
        create_ticket(issue, action)
        print(f"[{severity}] {issue['message']} -> {action}")
    
    time.sleep(config["check_interval"])
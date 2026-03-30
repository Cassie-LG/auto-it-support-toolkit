import json
from datetime import datetime

#Create structured ticket entries
def create_ticket(issue, action):
    ticket = {
        "timestamp": str(datetime.now()),
        "issue": issue["message"],
        "type": issue["type"],
        "action_taken": action,
        "status": "closed" if action else "open"
    }

    with open("tickets.json", "a") as f:
        f.write(json.dumps(ticket) + "\n")
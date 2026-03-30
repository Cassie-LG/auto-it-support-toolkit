from datetime import datetime

#Log issues to file
def log_event(event):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.now()} - {event}\n")
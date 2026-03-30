import os

#Attemp automatic fixes
def fix_issue(issue):
    if issue["type"] == "DISK":
        os.system("rm -rf /tmp/*")     #Clear temp files
        return "Cleared /tmp directory"
    elif issue["type"] == "CPU":
        return "Manual review recommended"
    elif issue["type"] == "PROCESS":
        os.system("service ssh start")
        return "Attempted to restart SSH"
    return "No action taken"
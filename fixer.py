import os
import platform

SYSTEM = platform.system()

#Attemp automatic fixes
def fix_issue(issue):
    if issue["type"] == "DISK":
        try:
            if SYSTEM == "Windows":
                os.system("del /q/f/s %TEMP%\\*")
                return "Cleared Windows temp files"
            else:
                os.system("rm -rf /tmp/*")     #Clear temp files
                return "Cleared /tmp directory"
        except Exception:
            return "Disk cleanup failed"
        
    elif issue["type"] == "CPU":
        return "Manual review recommended"
    
    elif issue["type"] == "PROCESS":
        try:
            if SYSTEM == "Windows":
                os.system("echo Attempted restart (simulated)")
                return "Simulated service restart (Windows)"
            else:
                os.system("systemctl restart ssh")
                return "Attempted to restart SSH"
        except Exception:
            return "Service restart failed"
        
    return "No action taken"
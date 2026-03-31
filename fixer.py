import os
import platform

SYSTEM = platform.system()

#Attemp automatic fixes
def fix_issue(issue):
    #Disk Fix
    if issue["type"] == "DISK":
        try:
            if SYSTEM == "Windows":
                os.system("del /q/f/s %TEMP%\\*")
                return "Cleared Windows temp files"
            else:
                os.system("rm -rf /tmp/*")
                return "Cleared /tmp directory"
        except Exception:
            return "Disk cleanup failed"

    #CPU Fix    
    elif issue["type"] == "CPU":
        return "Manual review recommended"
    
    #Process Fix
    elif issue["type"] == "PROCESS":
        try: 
            if SYSTEM == "Windows":
                return "Critical system process missing - manual intervention required"
            else:
                os.system("systemctl restart ssh")
                return "Attempted to restart SSH"
        except Exception:
            return "Service restart failed"
        
    return "No action taken"
import platform

#Choose process based on OS
SYSTEM = platform.system()
DEFAULT_SERVICE = "explorer" if SYSTEM == "Windows" else "ssh"

def detect_issues(stats, config):
    issues = []

    #CPU issue
    if stats["cpu"] > config["cpu_threshold"]:
        issues.append({"type": "CPU",
                       "message": "High CPU usage",
                       "severity": "HIGH"})

    #Memory issue
    if stats["memory"] > config["memory_threshold"]:
        issues.append({"type": "MEMORY",
                       "message": "High memory usage",
                       "severity": "HIGH"})

    #Disk issue
    if stats["disk"] > config["disk_threshold"]:
        issues.append({"type": "DISK",
                       "message": "Low disk space",
                       "severity": "CRITICAL"})

    #Process issue (ex. check if critical process is missing)
    running = [p[1] for p in stats["processes"]]
    if not any(DEFAULT_SERVICE in proc for proc in running):
        issues.append({"type": "PROCESS",
                       "message": f"{DEFAULT_SERVICE} service not running",
                       "severity": "CRITICAL"})

    return issues
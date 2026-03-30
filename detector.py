import platform

#Choose process based on OS
SYSTEM = platform.system()
DEFAULT_SERVICE = "explorer" if SYSTEM == "Windows" else "ssh"

def detect_issues(stats, config):
    issues = []

    #CPU issue
    if stats["cpu"] > config["cpu_threshold"]:
        issues.append({"type": "CPU", "message": "High CPU usage"})

    #Memory issue
    if stats["memory"] > config["memory_threshold"]:
        issues.append({"type": "MEMORY", "message": "High memory usage"})

    #Disk issue
    if stats["disk"] > config["disk_threshold"]:
        issues.append({"type": "DISK", "message": "Low disk space"})

    #Process issue (ex. check if critical process is missing)
    running = [p[1] for p in stats["processes"]]
    if DEFAULT_SERVICE not in running:
        issues.append({"type": "PROCESS", "message": f"{DEFAULT_SERVICE} service not running"})

    return issues
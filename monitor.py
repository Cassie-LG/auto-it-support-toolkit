import psutil
import os

# Cross-platform disk path
DISK_Path = "C:/" if os.name == "nt" else "/"

# Collect system stats
def get_system_stats():
    return {
        "cpu": psutil.cpu_percent(interval=1),     #CPU usage %
        "memory": psutil.virtual_memory().percent, #RAM usage %
        "disk": psutil.disk_usage(DISK_Path).percent,    #Disk usage %
        "processes": [(p.pid, p.info['name'], p.info['cpu_percent'])
                       for p in psutil.process_iter(['name', 'cpu_percent'])]
    }
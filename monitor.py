import psutil

# Collect system stats
def get_system_stats():
    return {
        "cpu": psutil.cpu_percent(interval=1),     #CPU usage %
        "memory": psutil.virtual_memory().percent, #RAM usage %
        "disk": psutil.disk_usage('/').percent,    #Disk usage %
        "processes": [(p.pid, p.info['name'], p.info['cpu_percent']) for p in psutil.process_iter(['name', 'cpu_percent'])]
    }
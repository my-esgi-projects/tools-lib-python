import psutil

def get_process_info():
    processes = []
    for process in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info']):
        try:
            info = process.info
            processes.append({
                'pid': info['pid'],
                'name': info['name'],
                'username': info['username'],
                'cpu_percent': info['cpu_percent'],
                'memory_info': info['memory_info'].rss
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes

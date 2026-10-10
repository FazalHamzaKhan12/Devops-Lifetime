import psutil

def get_system_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    system_info = {
        "CPU Usage": f"{cpu}%",
        "Memory Usage": f"{memory}%",
        "Disk Usage": f"{disk}%"
    }
    

    return system_info



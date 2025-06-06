import psutil
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    processes = len(psutil.pids())

    alerts = []

    if cpu > CPU_THRESHOLD:
        alerts.append(f"High CPU usage: {cpu}%")
    if memory > MEMORY_THRESHOLD:
        alerts.append(f"High Memory usage: {memory}%")
    if disk > DISK_THRESHOLD:
        alerts.append(f"Low Disk space: {disk}% used")

    if alerts:
        for alert in alerts:
            logging.warning(alert)
        print("⚠️ Alerts found! Check system_health.log")
    else:
        print(f"✅ System is healthy | CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%, Processes: {processes}")

if __name__ == "__main__":
    check_system_health()

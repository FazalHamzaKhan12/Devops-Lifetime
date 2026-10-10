import psutil

threshold = float(input("Enter the threshold value for CPU usage: "))

for i in range(5):
    if psutil.cpu_percent(interval=1) > threshold:
        print("CPU is unhealthy", psutil.cpu_percent(interval=1), "%")
    else:
        print("CPU usage is healthy")
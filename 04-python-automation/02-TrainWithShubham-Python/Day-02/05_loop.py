# Loop is a programming construct that allows you to repeat a block of code multiple times. In Python, there are two main types of loops: for loops and while loops.

import psutil

for i in range(5):
    print("CPU:", psutil.cpu_percent(interval=1), "%")
    print("RAM:", psutil.virtual_memory().percent, "%")
    if psutil.virtual_memory().percent > 60:
        print("RAM usage is high")
        break  # Exit the loop if RAM usage is high
    else:
        print("CPU usage is normal")


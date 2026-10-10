import psutil
import os

print("CPU:", psutil.cpu_percent(), "%")
print("RAM:", psutil.virtual_memory().percent, "%")

    
if psutil.virtual_memory().percent > 70:
    print("RAM usage is high")
    os.system("shutdown /r /t 15")  # This command will shut down the computer after 1 second

else:
    print("CPU usage is normal")



# print(dir(psutil)) #its give me all the methods and attributes of psutil module
# print(psutil.cpu_count.__doc__) # its explain the functionality of cpu_count method
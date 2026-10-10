import shutil
import datetime
import os

def backupfile(source, destination):
    today_time = datetime.date.today()
    backup_file_area = os.path.join(destination, f"backup_{today_time}")
    shutil.make_archive(backup_file_area, "gztar", source)
    
source = "C:/Users/DELL/Desktop/Python FOR Devops/TrainWithShubham_Python For Devops_4h_free_workshop/Day_01"
destination = "C:/Users/DELL/Desktop/Python FOR Devops/TrainWithShubham_Python For Devops_4h_free_workshop/Day_02/backup_usingpy/"


backupfile(source,destination)
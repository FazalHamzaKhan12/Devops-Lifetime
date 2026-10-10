import datetime
import os
import shutil


def filebackup_def(source, destination):
    today_time = datetime.date.today()
    backup_file_loc = os.path.join(destination, f"backup_{today_time}_loc")
    shutil.make_archive(backup_file_loc, "zip", source)
    
source = "C:/Users/DELL/Desktop/Python FOR Devops/TrainWithShubham_Python For Devops_4h_free_workshop/Day_01"
destination = "C:/Users/DELL/Desktop/Python FOR Devops/TrainWithShubham_Python For Devops_4h_free_workshop/Day_02/backup_usingpy/"

    
filebackup_def(source, destination)
    
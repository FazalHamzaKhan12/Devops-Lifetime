import datetime
import os
import shutil

def backup_def(source, destination):
    today = datetime.date.today()
    backup_file = os.path.join(destination, f"backupfiles{today}")
    shutil.make_archive(backup_file, "gztar", source)
    
    
source = "C:/Users/DELL/Desktop/Python FOR Devops/TrainWithShubham_Python For Devops_4h_free_workshop/Day_01"
destination = "C:/Users/DELL/Desktop/Python FOR Devops/TrainWithShubham_Python For Devops_4h_free_workshop/Day_02/backup_usingpy/"


backup_def(source, destination)
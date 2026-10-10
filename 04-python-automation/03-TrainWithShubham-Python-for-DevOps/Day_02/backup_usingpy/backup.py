import shutil
import datetime
import os


def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file_name.replace('.tar.gz', ''), 'gztar', source)
    
    
source = "C:/Users/DELL/Desktop/Python FOR Devops/TrainWithShubham_Python For Devops_4h_free_workshop/Day_01"
destination = "C:/Users/DELL/Desktop/Python FOR Devops/TrainWithShubham_Python For Devops_4h_free_workshop/Day_02/backup_usingpy/"

backup_files(source , destination)
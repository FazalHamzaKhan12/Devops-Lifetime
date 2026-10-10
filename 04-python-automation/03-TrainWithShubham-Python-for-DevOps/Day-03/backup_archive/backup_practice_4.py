import datetime
import os
import shutil

def backup_def(source, destination):
    today_time = datetime.date.today()
    backupfile_loc = os.path.join(destination, f"backup_{today_time}_loc")
    shutil.make_archive(backupfile_loc, "zip", source)


source = "C:/Users/Fazal Hamza Khan/Downloads/DevOPS/Python FOR Devops/TrainWithShubham_Python For Devops_4h_free_workshop/Day-02"
destination = "C:/Users/Fazal Hamza Khan/Downloads/DevOPS/Python FOR Devops/TrainWithShubham_Python For Devops_4h_free_workshop/Day-03/backup_archive/"


backup_def(source, destination)
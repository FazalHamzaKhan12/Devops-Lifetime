import datetime

# def checkcpu(command):
#     print(os.system(command))
    
# checkcpu('systeminfo')

def show_date():
    return datetime.datetime.today()

today = show_date()
print(today)

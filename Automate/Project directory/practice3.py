import schedule
import subprocess
import time
import datetime
from plyer import notification
from frontend1 import window3
from twilio1 import *



date_time = datetime.datetime.now()
current_time = date_time.strftime("%H:%M")
current_day = date_time.strftime("%A")

daylist = ["monlist", "tuelist", "wedlist",
           "thulist", "frilist", "satlist", "frilist"]

monlist = ["monsubnamelist", "monsubtimelist", "monsublinklist"]
monsubnamelist=[]
for i in range(10):
    monsubnamelist[i]=input()
    monsubnamelist.append(monsubnamelist[i])
monsubtimelist=[]
for j in range(10):
    monsubtimelist[j] = input()
    monsubtimelist.append(monsubtimelist[j])
monsublinklist=[]
for k in range(10):
    monsublinklist[k] = input()
    monsublinklist.append(monsublinklist[k])



tuelist = ["tuesubnamelist", "tuesubtimelist", "tuesublinklist"]
tuesubnamelist = []
for i in range(10):
    tuesubnamelist[i] = input()
    tuesubnamelist.append(tuesubnamelist[i])
tuesubtimelist = []
for j in range(10):
    tuesubtimelist[j] = input()
    tuesubtimelist.append(tuesubtimelist[j])
tuesublinklist = []
for k in range(10):
    tuesublinklist[k] = input()
    tuesublinklist.append(tuesublinklist[k])



wedlist = ["wedsubnamelist", "wedsubtimelist", "wedsublinklist"]
wedsubnamelist = []
for i in range(10):
    wedsubnamelist[i] = input()
    wedsubnamelist.append(wedsubnamelist[i])
wedsubtimelist = []
for j in range(10):
    wedsubtimelist[j] = input()
    wedsubtimelist.append(wedsubtimelist[j])
wedsublinklist = []
for k in range(10):
    wedsublinklist[k] = input()
    wedsublinklist.append(wedsublinklist[k])



thulist = ["thusubnamelist", "thusubtimelist", "thusublinklist"]
thusubnamelist = []
for i in range(10):
    thusubnamelist[i] = input()
    thusubnamelist.append(thusubnamelist[i])
thusubtimelist = []
for j in range(10):
    thusubtimelist[j] = input()
    thusubtimelist.append(thusubtimelist[j])
thusublinklist = []
for k in range(10):
    thusublinklist[k] = input()
    thusublinklist.append(thusublinklist[k])



frilist = ["frisubnamelist", "frisubtimelist", "frisublinklist"]
frisubnamelist = []
for i in range(10):
    frisubnamelist[i] = input()
    frisubnamelist.append(frisubnamelist[i])
frisubtimelist = []
for j in range(10):
    frisubtimelist[j] = input()
    frisubtimelist.append(frisubtimelist[j])
frisublinklist = []
for k in range(10):
    frisublinklist[k] = input()
    frisublinklist.append(frisublinklist[k])



satlist = ["satsubnamelist", "satsubtimelist", "satsublinklist"]
satsubnamelist = []
for i in range(10):
    satsubnamelist[i] = input()
    satsubnamelist.append(satsubnamelist[i])
satsubtimelist = []
for j in range(10):
    satsubtimelist[j] = input()
    satsubtimelist.append(satsubtimelist[j])
satsublinklist = []
for k in range(10):
    satsublinklist[k] = input()
    satsublinklist.append(satsublinklist[k])



sunlist = ["sunsubnamelist", "sunsubtimelist", "sunsublinklist"]
sunsubnamelist = []
for i in range(10):
    sunsubnamelist[i] = input()
    sunsubnamelist.append(sunsubnamelist[i])
sunsubtimelist = []
for j in range(10):
    sunsubtimelist[j] = input()
    sunsubtimelist.append(sunsubtimelist[j])
sunsublinklist = []
for k in range(10):
    sunsublinklist[k] = input()
    sunsublinklist.append(sunsublinklist[k])





#a student can schedule a max of 10 classes per day


def chrome(link):
    Call_URL = link
    mycmd = r'start chrome /new-tab {}'.format(Call_URL)
    subprocess.Popen(mycmd, shell=True)


def ntn():
    notification.notify(
        title="AUTOMATE",
        message=f"you have a class in {window3.notifytime.get()} minutes ",
        app_name="AUTOMATE",
        app_icon="3xhumed-Mega-Games-Pack-38-Prey-logo-1.ico",
        timeout=10,
        ticker="classtime",
        toast=False,
    )


    



if ((current_time == monlist[1][0]-window3.notifytime.get()) and (current_day == "Monday")) or ((current_time == tuelist[1][0]-window3.notifytime.get()) and (current_day == "Tuesday")) or ((current_time == wedlist[1][0]-window3.notifytime.get()) and (current_day == "Wednesday")) or ((current_time == thulist[1][0]-window3.notifytime.get()) and (current_day == "Thursday")) or ((current_time == frilist[1][0]-window3.notifytime.get()) and (current_day == "Friday")) or ((current_time == satlist[1][0]-window3.notifytime.get()) and (current_day == "Saturday")) or ((current_time == sunlist[1][0]-window3.notifytime.get()) and (current_day == "Sunday")):
    
    schedule.every().monday.at(monlist[1][0]-window3.notifytime.get()).do(ntn)
    schedule.every().tuesday.at(tuelist[1][0]-window3.notifytime.get()).do(ntn)
    schedule.every().wednesday.at(wedlist[1][0]-window3.notifytime.get()).do(ntn)
    schedule.every().thursday.at(thulist[1][0]-window3.notifytime.get()).do(ntn)
    schedule.every().friday.at(frilist[1][0]-window3.notifytime.get()).do(ntn)
    schedule.every().saturday.at(satlist[1][0]-window3.notifytime.get()).do(ntn)
    schedule.every().sunday.at(sunlist[1][0]-window3.notifytime.get()).do(ntn)

    schedule.every().monday.at(monlist[1][0]-window3.notifytime.get()).do(twilionotify)
    schedule.every().tuesday.at(tuelist[1][0]-window3.notifytime.get()).do(twilionotify)
    schedule.every().wednesday.at(wedlist[1][0]-window3.notifytime.get()).do(twilionotify)
    schedule.every().thursday.at(thulist[1][0]-window3.notifytime.get()).do(twilionotify)
    schedule.every().friday.at(frilist[1][0]-window3.notifytime.get()).do(twilionotify)
    schedule.every().saturday.at(satlist[1][0]-window3.notifytime.get()).do(twilionotify)
    schedule.every().sunday.at(sunlist[1][0]-window3.notifytime.get()).do(twilionotify)
    while True:
        schedule.run_pending()
elif ((current_time == monlist[1][0]) and (current_day == "Monday")) or ((current_time == tuelist[1][0]) and (current_day == "Tuesday")) or ((current_time == wedlist[1][0]) and (current_day == "Wednesday")) or ((current_time == thulist[1][0]) and (current_day == "Thursday")) or ((current_time == frilist[1][0]) and (current_day == "Friday")) or ((current_time == satlist[1][0]) and (current_day == "Saturday")) or ((current_time == sunlist[1][0]) and (current_day == "Sunday")):
    schedule.every().monday.at(monlist[1][0]).do(chrome(monlist[2][0]))
    schedule.every().tuesday.at(tuelist[1][0]).do(chrome(tuelist[2][0]))
    schedule.every().wednesday.at(wedlist[1][0]).do(chrome(wedlist[2][0]))
    schedule.every().monday.at(thulist[1][0]).do(chrome(thulist[2][0]))
    schedule.every().tuesday.at(frilist[1][0]).do(chrome(frilist[2][0]))
    schedule.every().wednesday.at(satlist[1][0]).do(chrome(satlist[2][0]))
    schedule.every().wednesday.at(sunlist[1][0]).do(chrome(sunlist[2][0]))
    while True:
        schedule.run_pending()
        time.sleep(1)
elif ((current_time == monlist[1][1]-window3.notifytime.get()) and (current_day == "Monday")) or ((current_time == tuelist[1][1]-window3.notifytime.get()) and (current_day == "Tuesday")) or ((current_time == wedlist[1][1]-window3.notifytime.get()) and (current_day == "Wednesday")) or ((current_time == thulist[1][1]-window3.notifytime.get()) and (current_day == "Thursday")) or ((current_time == frilist[1][1]-window3.notifytime.get()) and (current_day == "Friday")) or ((current_time == satlist[1][1]-window3.notifytime.get()) and (current_day == "Saturday")) or ((current_time == sunlist[1][1]-window3.notifytime.get()) and (current_day == "Sunday")):

    schedule.every().monday.at(monlist[1][1]-window3.notifytime.get()).do(ntn)
    schedule.every().tuesday.at(tuelist[1][1]-window3.notifytime.get()).do(ntn)
    schedule.every().wednesday.at(wedlist[1][1]-window3.notifytime.get()).do(ntn)
    schedule.every().thursday.at(thulist[1][1]-window3.notifytime.get()).do(ntn)
    schedule.every().friday.at(frilist[1][1]-window3.notifytime.get()).do(ntn)
    schedule.every().saturday.at(satlist[1][1]-window3.notifytime.get()).do(ntn)
    schedule.every().sunday.at(sunlist[1][1]-window3.notifytime.get()).do(ntn)

    schedule.every().monday.at(monlist[1][1]-window3.notifytime.get()).do(twilionotify)
    schedule.every().tuesday.at(tuelist[1][1]-window3.notifytime.get()).do(twilionotify)
    schedule.every().wednesday.at(wedlist[1][1]-window3.notifytime.get()).do(twilionotify)
    schedule.every().thursday.at(thulist[1][1]-window3.notifytime.get()).do(twilionotify)
    schedule.every().friday.at(frilist[1][1]-window3.notifytime.get()).do(twilionotify)
    schedule.every().saturday.at(satlist[1][1]-window3.notifytime.get()).do(twilionotify)
    schedule.every().sunday.at(sunlist[1][1]-window3.notifytime.get()).do(twilionotify)
    while True:
        schedule.run_pending()
elif ((current_time == monlist[1][1]) and (current_day == "Monday")) or ((current_time == tuelist[1][1]) and (current_day == "Tuesday")) or ((current_time == wedlist[1][1]) and (current_day == "Wednesday")) or ((current_time == thulist[1][1]) and (current_day == "Thursday")) or ((current_time == frilist[1][1]) and (current_day == "Friday")) or ((current_time == satlist[1][1]) and (current_day == "Saturday")) or ((current_time == sunlist[1][1]) and (current_day == "Sunday")):
    schedule.every().monday.at(monlist[1][1]).do(chrome(monlist[2][1]))
    schedule.every().tuesday.at(tuelist[1][1]).do(chrome(tuelist[2][1]))
    schedule.every().wednesday.at(wedlist[1][1]).do(chrome(wedlist[2][1]))
    schedule.every().monday.at(thulist[1][1]).do(chrome(thulist[2][1]))
    schedule.every().tuesday.at(frilist[1][1]).do(chrome(frilist[2][1]))
    schedule.every().wednesday.at(satlist[1][1]).do(chrome(satlist[2][1]))
    schedule.every().wednesday.at(sunlist[1][1]).do(chrome(sunlist[2][1]))
    while True:
        schedule.run_pending()
        time.sleep(1)
elif ((current_time == monlist[1][2]-window3.notifytime.get()) and (current_day == "Monday")) or ((current_time == tuelist[1][2]-window3.notifytime.get()) and (current_day == "Tuesday")) or ((current_time == wedlist[1][2]-window3.notifytime.get()) and (current_day == "Wednesday")) or ((current_time == thulist[1][2]-window3.notifytime.get()) and (current_day == "Thursday")) or ((current_time == frilist[1][2]-window3.notifytime.get()) and (current_day == "Friday")) or ((current_time == satlist[1][2]-window3.notifytime.get()) and (current_day == "Saturday")) or ((current_time == sunlist[1][2]-window3.notifytime.get()) and (current_day == "Sunday")):

    schedule.every().monday.at(monlist[1][2]-window3.notifytime.get()).do(ntn)
    schedule.every().tuesday.at(tuelist[1][2]-window3.notifytime.get()).do(ntn)
    schedule.every().wednesday.at(
        wedlist[1][2]-window3.notifytime.get()).do(ntn)
    schedule.every().thursday.at(
        thulist[1][2]-window3.notifytime.get()).do(ntn)
    schedule.every().friday.at(frilist[1][2]-window3.notifytime.get()).do(ntn)
    schedule.every().saturday.at(
        satlist[1][2]-window3.notifytime.get()).do(ntn)
    schedule.every().sunday.at(sunlist[1][2]-window3.notifytime.get()).do(ntn)

    schedule.every().monday.at(
        monlist[1][2]-window3.notifytime.get()).do(twilionotify)
    schedule.every().tuesday.at(
        tuelist[1][2]-window3.notifytime.get()).do(twilionotify)
    schedule.every().wednesday.at(
        wedlist[1][2]-window3.notifytime.get()).do(twilionotify)
    schedule.every().thursday.at(
        thulist[1][2]-window3.notifytime.get()).do(twilionotify)
    schedule.every().friday.at(
        frilist[1][2]-window3.notifytime.get()).do(twilionotify)
    schedule.every().saturday.at(
        satlist[1][2]-window3.notifytime.get()).do(twilionotify)
    schedule.every().sunday.at(
        sunlist[1][2]-window3.notifytime.get()).do(twilionotify)
    while True:
        schedule.run_pending()
elif ((current_time == monlist[1][2]) and (current_day == "Monday")) or ((current_time == tuelist[1][2]) and (current_day == "Tuesday")) or ((current_time == wedlist[1][2]) and (current_day == "Wednesday")) or ((current_time == thulist[1][2]) and (current_day == "Thursday")) or ((current_time == frilist[1][2]) and (current_day == "Friday")) or ((current_time == satlist[1][2]) and (current_day == "Saturday")) or ((current_time == sunlist[1][2]) and (current_day == "Sunday")):
    schedule.every().monday.at(monlist[1][2]).do(chrome(monlist[2][2]))
    schedule.every().tuesday.at(tuelist[1][2]).do(chrome(tuelist[2][2]))
    schedule.every().wednesday.at(wedlist[1][2]).do(chrome(wedlist[2][2]))
    schedule.every().monday.at(thulist[1][2]).do(chrome(thulist[2][2]))
    schedule.every().tuesday.at(frilist[1][2]).do(chrome(frilist[2][2]))
    schedule.every().wednesday.at(satlist[1][2]).do(chrome(satlist[2][2]))
    schedule.every().wednesday.at(sunlist[1][2]).do(chrome(sunlist[2][2]))
    while True:
        schedule.run_pending()
        time.sleep(1)
elif ((current_time == monlist[1][3]-window3.notifytime.get()) and (current_day == "Monday")) or ((current_time == tuelist[1][3]-window3.notifytime.get()) and (current_day == "Tuesday")) or ((current_time == wedlist[1][3]-window3.notifytime.get()) and (current_day == "Wednesday")) or ((current_time == thulist[1][3]-window3.notifytime.get()) and (current_day == "Thursday")) or ((current_time == frilist[1][3]-window3.notifytime.get()) and (current_day == "Friday")) or ((current_time == satlist[1][3]-window3.notifytime.get()) and (current_day == "Saturday")) or ((current_time == sunlist[1][3]-window3.notifytime.get()) and (current_day == "Sunday")):

    schedule.every().monday.at(monlist[1][3]-window3.notifytime.get()).do(ntn)
    schedule.every().tuesday.at(tuelist[1][3]-window3.notifytime.get()).do(ntn)
    schedule.every().wednesday.at(
        wedlist[1][3]-window3.notifytime.get()).do(ntn)
    schedule.every().thursday.at(
        thulist[1][3]-window3.notifytime.get()).do(ntn)
    schedule.every().friday.at(frilist[1][3]-window3.notifytime.get()).do(ntn)
    schedule.every().saturday.at(
        satlist[1][3]-window3.notifytime.get()).do(ntn)
    schedule.every().sunday.at(sunlist[1][3]-window3.notifytime.get()).do(ntn)

    schedule.every().monday.at(
        monlist[1][3]-window3.notifytime.get()).do(twilionotify)
    schedule.every().tuesday.at(
        tuelist[1][3]-window3.notifytime.get()).do(twilionotify)
    schedule.every().wednesday.at(
        wedlist[1][3]-window3.notifytime.get()).do(twilionotify)
    schedule.every().thursday.at(
        thulist[1][3]-window3.notifytime.get()).do(twilionotify)
    schedule.every().friday.at(
        frilist[1][3]-window3.notifytime.get()).do(twilionotify)
    schedule.every().saturday.at(
        satlist[1][3]-window3.notifytime.get()).do(twilionotify)
    schedule.every().sunday.at(
        sunlist[1][3]-window3.notifytime.get()).do(twilionotify)
    while True:
        schedule.run_pending()
elif ((current_time == monlist[1][3]) and (current_day == "Monday")) or ((current_time == tuelist[1][3]) and (current_day == "Tuesday")) or ((current_time == wedlist[1][3]) and (current_day == "Wednesday")) or ((current_time == thulist[1][3]) and (current_day == "Thursday")) or ((current_time == frilist[1][3]) and (current_day == "Friday")) or ((current_time == satlist[1][3]) and (current_day == "Saturday")) or ((current_time == sunlist[1][3]) and (current_day == "Sunday")):
    schedule.every().monday.at(monlist[1][3]).do(chrome(monlist[2][3]))
    schedule.every().tuesday.at(tuelist[1][3]).do(chrome(tuelist[2][3]))
    schedule.every().wednesday.at(wedlist[1][3]).do(chrome(wedlist[2][3]))
    schedule.every().monday.at(thulist[1][3]).do(chrome(thulist[2][3]))
    schedule.every().tuesday.at(frilist[1][3]).do(chrome(frilist[2][3]))
    schedule.every().wednesday.at(satlist[1][3]).do(chrome(satlist[2][3]))
    schedule.every().wednesday.at(sunlist[1][3]).do(chrome(sunlist[2][3]))
    while True:
        schedule.run_pending()
        time.sleep(1)
elif ((current_time == monlist[1][4]-window3.notifytime.get()) and (current_day == "Monday")) or ((current_time == tuelist[1][4]-window3.notifytime.get()) and (current_day == "Tuesday")) or ((current_time == wedlist[1][4]-window3.notifytime.get()) and (current_day == "Wednesday")) or ((current_time == thulist[1][4]-window3.notifytime.get()) and (current_day == "Thursday")) or ((current_time == frilist[1][4]-window3.notifytime.get()) and (current_day == "Friday")) or ((current_time == satlist[1][4]-window3.notifytime.get()) and (current_day == "Saturday")) or ((current_time == sunlist[1][4]-window3.notifytime.get()) and (current_day == "Sunday")):

    schedule.every().monday.at(monlist[1][4]-window3.notifytime.get()).do(ntn)
    schedule.every().tuesday.at(tuelist[1][4]-window3.notifytime.get()).do(ntn)
    schedule.every().wednesday.at(
        wedlist[1][4]-window3.notifytime.get()).do(ntn)
    schedule.every().thursday.at(
        thulist[1][4]-window3.notifytime.get()).do(ntn)
    schedule.every().friday.at(frilist[1][4]-window3.notifytime.get()).do(ntn)
    schedule.every().saturday.at(
        satlist[1][4]-window3.notifytime.get()).do(ntn)
    schedule.every().sunday.at(sunlist[1][4]-window3.notifytime.get()).do(ntn)

    schedule.every().monday.at(
        monlist[1][4]-window3.notifytime.get()).do(twilionotify)
    schedule.every().tuesday.at(
        tuelist[1][4]-window3.notifytime.get()).do(twilionotify)
    schedule.every().wednesday.at(
        wedlist[1][4]-window3.notifytime.get()).do(twilionotify)
    schedule.every().thursday.at(
        thulist[1][4]-window3.notifytime.get()).do(twilionotify)
    schedule.every().friday.at(
        frilist[1][4]-window3.notifytime.get()).do(twilionotify)
    schedule.every().saturday.at(
        satlist[1][4]-window3.notifytime.get()).do(twilionotify)
    schedule.every().sunday.at(
        sunlist[1][4]-window3.notifytime.get()).do(twilionotify)
    while True:
        schedule.run_pending()
elif ((current_time == monlist[1][4]) and (current_day == "Monday")) or ((current_time == tuelist[1][4]) and (current_day == "Tuesday")) or ((current_time == wedlist[1][4]) and (current_day == "Wednesday")) or ((current_time == thulist[1][4]) and (current_day == "Thursday")) or ((current_time == frilist[1][4]) and (current_day == "Friday")) or ((current_time == satlist[1][4]) and (current_day == "Saturday")) or ((current_time == sunlist[1][4]) and (current_day == "Sunday")):
    schedule.every().monday.at(monlist[1][4]).do(chrome(monlist[2][4]))
    schedule.every().tuesday.at(tuelist[1][4]).do(chrome(tuelist[2][4]))
    schedule.every().wednesday.at(wedlist[1][4]).do(chrome(wedlist[2][4]))
    schedule.every().monday.at(thulist[1][4]).do(chrome(thulist[2][4]))
    schedule.every().tuesday.at(frilist[1][4]).do(chrome(frilist[2][4]))
    schedule.every().wednesday.at(satlist[1][4]).do(chrome(satlist[2][4]))
    schedule.every().wednesday.at(sunlist[1][4]).do(chrome(sunlist[2][4]))
    while True:
        schedule.run_pending()
        time.sleep(1)
elif ((current_time == monlist[1][5]-window3.notifytime.get()) and (current_day == "Monday")) or ((current_time == tuelist[1][5]-window3.notifytime.get()) and (current_day == "Tuesday")) or ((current_time == wedlist[1][5]-window3.notifytime.get()) and (current_day == "Wednesday")) or ((current_time == thulist[1][5]-window3.notifytime.get()) and (current_day == "Thursday")) or ((current_time == frilist[1][5]-window3.notifytime.get()) and (current_day == "Friday")) or ((current_time == satlist[1][5]-window3.notifytime.get()) and (current_day == "Saturday")) or ((current_time == sunlist[1][5]-window3.notifytime.get()) and (current_day == "Sunday")):

    schedule.every().monday.at(monlist[1][5]-window3.notifytime.get()).do(ntn)
    schedule.every().tuesday.at(tuelist[1][5]-window3.notifytime.get()).do(ntn)
    schedule.every().wednesday.at(
        wedlist[1][5]-window3.notifytime.get()).do(ntn)
    schedule.every().thursday.at(
        thulist[1][5]-window3.notifytime.get()).do(ntn)
    schedule.every().friday.at(frilist[1][5]-window3.notifytime.get()).do(ntn)
    schedule.every().saturday.at(
        satlist[1][5]-window3.notifytime.get()).do(ntn)
    schedule.every().sunday.at(sunlist[1][5]-window3.notifytime.get()).do(ntn)

    schedule.every().monday.at(
        monlist[1][5]-window3.notifytime.get()).do(twilionotify)
    schedule.every().tuesday.at(
        tuelist[1][5]-window3.notifytime.get()).do(twilionotify)
    schedule.every().wednesday.at(
        wedlist[1][5]-window3.notifytime.get()).do(twilionotify)
    schedule.every().thursday.at(
        thulist[1][5]-window3.notifytime.get()).do(twilionotify)
    schedule.every().friday.at(
        frilist[1][5]-window3.notifytime.get()).do(twilionotify)
    schedule.every().saturday.at(
        satlist[1][5]-window3.notifytime.get()).do(twilionotify)
    schedule.every().sunday.at(
        sunlist[1][5]-window3.notifytime.get()).do(twilionotify)
    while True:
        schedule.run_pending()
elif ((current_time == monlist[1][5]) and (current_day == "Monday")) or ((current_time == tuelist[1][5]) and (current_day == "Tuesday")) or ((current_time == wedlist[1][5]) and (current_day == "Wednesday")) or ((current_time == thulist[1][5]) and (current_day == "Thursday")) or ((current_time == frilist[1][5]) and (current_day == "Friday")) or ((current_time == satlist[1][5]) and (current_day == "Saturday")) or ((current_time == sunlist[1][5]) and (current_day == "Sunday")):
    schedule.every().monday.at(monlist[1][5]).do(chrome(monlist[2][5]))
    schedule.every().tuesday.at(tuelist[1][5]).do(chrome(tuelist[2][5]))
    schedule.every().wednesday.at(wedlist[1][5]).do(chrome(wedlist[2][5]))
    schedule.every().monday.at(thulist[1][5]).do(chrome(thulist[2][5]))
    schedule.every().tuesday.at(frilist[1][5]).do(chrome(frilist[2][5]))
    schedule.every().wednesday.at(satlist[1][5]).do(chrome(satlist[2][5]))
    schedule.every().wednesday.at(sunlist[1][5]).do(chrome(sunlist[2][5]))
    while True:
        schedule.run_pending()
        time.sleep(1)
elif ((current_time == monlist[1][6]-window3.notifytime.get()) and (current_day == "Monday")) or ((current_time == tuelist[1][6]-window3.notifytime.get()) and (current_day == "Tuesday")) or ((current_time == wedlist[1][6]-window3.notifytime.get()) and (current_day == "Wednesday")) or ((current_time == thulist[1][6]-window3.notifytime.get()) and (current_day == "Thursday")) or ((current_time == frilist[1][6]-window3.notifytime.get()) and (current_day == "Friday")) or ((current_time == satlist[1][6]-window3.notifytime.get()) and (current_day == "Saturday")) or ((current_time == sunlist[1][6]-window3.notifytime.get()) and (current_day == "Sunday")):

    schedule.every().monday.at(monlist[1][6]-window3.notifytime.get()).do(ntn)
    schedule.every().tuesday.at(tuelist[1][6]-window3.notifytime.get()).do(ntn)
    schedule.every().wednesday.at(
        wedlist[1][6]-window3.notifytime.get()).do(ntn)
    schedule.every().thursday.at(
        thulist[1][6]-window3.notifytime.get()).do(ntn)
    schedule.every().friday.at(frilist[1][6]-window3.notifytime.get()).do(ntn)
    schedule.every().saturday.at(
        satlist[1][6]-window3.notifytime.get()).do(ntn)
    schedule.every().sunday.at(sunlist[1][6]-window3.notifytime.get()).do(ntn)

    schedule.every().monday.at(
        monlist[1][6]-window3.notifytime.get()).do(twilionotify)
    schedule.every().tuesday.at(
        tuelist[1][6]-window3.notifytime.get()).do(twilionotify)
    schedule.every().wednesday.at(
        wedlist[1][6]-window3.notifytime.get()).do(twilionotify)
    schedule.every().thursday.at(
        thulist[1][6]-window3.notifytime.get()).do(twilionotify)
    schedule.every().friday.at(
        frilist[1][6]-window3.notifytime.get()).do(twilionotify)
    schedule.every().saturday.at(
        satlist[1][6]-window3.notifytime.get()).do(twilionotify)
    schedule.every().sunday.at(
        sunlist[1][6]-window3.notifytime.get()).do(twilionotify)
    while True:
        schedule.run_pending()
elif ((current_time == monlist[1][6]) and (current_day == "Monday")) or ((current_time == tuelist[1][6]) and (current_day == "Tuesday")) or ((current_time == wedlist[1][6]) and (current_day == "Wednesday")) or ((current_time == thulist[1][6]) and (current_day == "Thursday")) or ((current_time == frilist[1][6]) and (current_day == "Friday")) or ((current_time == satlist[1][6]) and (current_day == "Saturday")) or ((current_time == sunlist[1][6]) and (current_day == "Sunday")):
    schedule.every().monday.at(monlist[1][6]).do(chrome(monlist[2][6]))
    schedule.every().tuesday.at(tuelist[1][6]).do(chrome(tuelist[2][6]))
    schedule.every().wednesday.at(wedlist[1][6]).do(chrome(wedlist[2][6]))
    schedule.every().monday.at(thulist[1][6]).do(chrome(thulist[2][6]))
    schedule.every().tuesday.at(frilist[1][6]).do(chrome(frilist[2][6]))
    schedule.every().wednesday.at(satlist[1][6]).do(chrome(satlist[2][6]))
    schedule.every().wednesday.at(sunlist[1][6]).do(chrome(sunlist[2][6]))
    while True:
        schedule.run_pending()
        time.sleep(1)
elif ((current_time == monlist[1][7]-window3.notifytime.get()) and (current_day == "Monday")) or ((current_time == tuelist[1][7]-window3.notifytime.get()) and (current_day == "Tuesday")) or ((current_time == wedlist[1][7]-window3.notifytime.get()) and (current_day == "Wednesday")) or ((current_time == thulist[1][7]-window3.notifytime.get()) and (current_day == "Thursday")) or ((current_time == frilist[1][7]-window3.notifytime.get()) and (current_day == "Friday")) or ((current_time == satlist[1][7]-window3.notifytime.get()) and (current_day == "Saturday")) or ((current_time == sunlist[1][7]-window3.notifytime.get()) and (current_day == "Sunday")):

    schedule.every().monday.at(monlist[1][7]-window3.notifytime.get()).do(ntn)
    schedule.every().tuesday.at(tuelist[1][7]-window3.notifytime.get()).do(ntn)
    schedule.every().wednesday.at(
        wedlist[1][7]-window3.notifytime.get()).do(ntn)
    schedule.every().thursday.at(
        thulist[1][7]-window3.notifytime.get()).do(ntn)
    schedule.every().friday.at(frilist[1][7]-window3.notifytime.get()).do(ntn)
    schedule.every().saturday.at(
        satlist[1][7]-window3.notifytime.get()).do(ntn)
    schedule.every().sunday.at(sunlist[1][7]-window3.notifytime.get()).do(ntn)

    schedule.every().monday.at(
        monlist[1][7]-window3.notifytime.get()).do(twilionotify)
    schedule.every().tuesday.at(
        tuelist[1][7]-window3.notifytime.get()).do(twilionotify)
    schedule.every().wednesday.at(
        wedlist[1][7]-window3.notifytime.get()).do(twilionotify)
    schedule.every().thursday.at(
        thulist[1][7]-window3.notifytime.get()).do(twilionotify)
    schedule.every().friday.at(
        frilist[1][7]-window3.notifytime.get()).do(twilionotify)
    schedule.every().saturday.at(
        satlist[1][7]-window3.notifytime.get()).do(twilionotify)
    schedule.every().sunday.at(
        sunlist[1][7]-window3.notifytime.get()).do(twilionotify)
    while True:
        schedule.run_pending()
elif ((current_time == monlist[1][7]) and (current_day == "Monday")) or ((current_time == tuelist[1][7]) and (current_day == "Tuesday")) or ((current_time == wedlist[1][7]) and (current_day == "Wednesday")) or ((current_time == thulist[1][7]) and (current_day == "Thursday")) or ((current_time == frilist[1][7]) and (current_day == "Friday")) or ((current_time == satlist[1][7]) and (current_day == "Saturday")) or ((current_time == sunlist[1][7]) and (current_day == "Sunday")):
    schedule.every().monday.at(monlist[1][7]).do(chrome(monlist[2][7]))
    schedule.every().tuesday.at(tuelist[1][7]).do(chrome(tuelist[2][7]))
    schedule.every().wednesday.at(wedlist[1][7]).do(chrome(wedlist[2][7]))
    schedule.every().monday.at(thulist[1][7]).do(chrome(thulist[2][7]))
    schedule.every().tuesday.at(frilist[1][7]).do(chrome(frilist[2][7]))
    schedule.every().wednesday.at(satlist[1][7]).do(chrome(satlist[2][7]))
    schedule.every().wednesday.at(sunlist[1][7]).do(chrome(sunlist[2][7]))
    while True:
        schedule.run_pending()
        time.sleep(1)
elif ((current_time == monlist[1][8]-window3.notifytime.get()) and (current_day == "Monday")) or ((current_time == tuelist[1][8]-window3.notifytime.get()) and (current_day == "Tuesday")) or ((current_time == wedlist[1][8]-window3.notifytime.get()) and (current_day == "Wednesday")) or ((current_time == thulist[1][8]-window3.notifytime.get()) and (current_day == "Thursday")) or ((current_time == frilist[1][8]-window3.notifytime.get()) and (current_day == "Friday")) or ((current_time == satlist[1][8]-window3.notifytime.get()) and (current_day == "Saturday")) or ((current_time == sunlist[1][8]-window3.notifytime.get()) and (current_day == "Sunday")):

    schedule.every().monday.at(monlist[1][8]-window3.notifytime.get()).do(ntn)
    schedule.every().tuesday.at(tuelist[1][8]-window3.notifytime.get()).do(ntn)
    schedule.every().wednesday.at(
        wedlist[1][8]-window3.notifytime.get()).do(ntn)
    schedule.every().thursday.at(
        thulist[1][8]-window3.notifytime.get()).do(ntn)
    schedule.every().friday.at(frilist[1][8]-window3.notifytime.get()).do(ntn)
    schedule.every().saturday.at(
        satlist[1][8]-window3.notifytime.get()).do(ntn)
    schedule.every().sunday.at(sunlist[1][8]-window3.notifytime.get()).do(ntn)

    schedule.every().monday.at(
        monlist[1][8]-window3.notifytime.get()).do(twilionotify)
    schedule.every().tuesday.at(
        tuelist[1][8]-window3.notifytime.get()).do(twilionotify)
    schedule.every().wednesday.at(
        wedlist[1][8]-window3.notifytime.get()).do(twilionotify)
    schedule.every().thursday.at(
        thulist[1][8]-window3.notifytime.get()).do(twilionotify)
    schedule.every().friday.at(
        frilist[1][8]-window3.notifytime.get()).do(twilionotify)
    schedule.every().saturday.at(
        satlist[1][8]-window3.notifytime.get()).do(twilionotify)
    schedule.every().sunday.at(
        sunlist[1][8]-window3.notifytime.get()).do(twilionotify)
    while True:
        schedule.run_pending()
elif ((current_time == monlist[1][8]) and (current_day == "Monday")) or ((current_time == tuelist[1][8]) and (current_day == "Tuesday")) or ((current_time == wedlist[1][8]) and (current_day == "Wednesday")) or ((current_time == thulist[1][8]) and (current_day == "Thursday")) or ((current_time == frilist[1][8]) and (current_day == "Friday")) or ((current_time == satlist[1][8]) and (current_day == "Saturday")) or ((current_time == sunlist[1][8]) and (current_day == "Sunday")):
    schedule.every().monday.at(monlist[1][8]).do(chrome(monlist[2][8]))
    schedule.every().tuesday.at(tuelist[1][8]).do(chrome(tuelist[2][8]))
    schedule.every().wednesday.at(wedlist[1][8]).do(chrome(wedlist[2][8]))
    schedule.every().monday.at(thulist[1][8]).do(chrome(thulist[2][8]))
    schedule.every().tuesday.at(frilist[1][8]).do(chrome(frilist[2][8]))
    schedule.every().wednesday.at(satlist[1][8]).do(chrome(satlist[2][8]))
    schedule.every().wednesday.at(sunlist[1][8]).do(chrome(sunlist[2][8]))
    while True:
        schedule.run_pending()
        time.sleep(1)
elif ((current_time == monlist[1][9]-window3.notifytime.get()) and (current_day == "Monday")) or ((current_time == tuelist[1][9]-window3.notifytime.get()) and (current_day == "Tuesday")) or ((current_time == wedlist[1][9]-window3.notifytime.get()) and (current_day == "Wednesday")) or ((current_time == thulist[1][9]-window3.notifytime.get()) and (current_day == "Thursday")) or ((current_time == frilist[1][9]-window3.notifytime.get()) and (current_day == "Friday")) or ((current_time == satlist[1][9]-window3.notifytime.get()) and (current_day == "Saturday")) or ((current_time == sunlist[1][9]-window3.notifytime.get()) and (current_day == "Sunday")):

    schedule.every().monday.at(monlist[1][9]-window3.notifytime.get()).do(ntn)
    schedule.every().tuesday.at(tuelist[1][9]-window3.notifytime.get()).do(ntn)
    schedule.every().wednesday.at(
        wedlist[1][9]-window3.notifytime.get()).do(ntn)
    schedule.every().thursday.at(
        thulist[1][9]-window3.notifytime.get()).do(ntn)
    schedule.every().friday.at(frilist[1][9]-window3.notifytime.get()).do(ntn)
    schedule.every().saturday.at(
        satlist[1][9]-window3.notifytime.get()).do(ntn)
    schedule.every().sunday.at(sunlist[1][9]-window3.notifytime.get()).do(ntn)

    schedule.every().monday.at(
        monlist[1][9]-window3.notifytime.get()).do(twilionotify)
    schedule.every().tuesday.at(
        tuelist[1][9]-window3.notifytime.get()).do(twilionotify)
    schedule.every().wednesday.at(
        wedlist[1][9]-window3.notifytime.get()).do(twilionotify)
    schedule.every().thursday.at(
        thulist[1][9]-window3.notifytime.get()).do(twilionotify)
    schedule.every().friday.at(
        frilist[1][9]-window3.notifytime.get()).do(twilionotify)
    schedule.every().saturday.at(
        satlist[1][9]-window3.notifytime.get()).do(twilionotify)
    schedule.every().sunday.at(
        sunlist[1][9]-window3.notifytime.get()).do(twilionotify)
    while True:
        schedule.run_pending()
elif ((current_time == monlist[1][9]) and (current_day == "Monday")) or ((current_time == tuelist[1][9]) and (current_day == "Tuesday")) or ((current_time == wedlist[1][9]) and (current_day == "Wednesday")) or ((current_time == thulist[1][9]) and (current_day == "Thursday")) or ((current_time == frilist[1][9]) and (current_day == "Friday")) or ((current_time == satlist[1][9]) and (current_day == "Saturday")) or ((current_time == sunlist[1][9]) and (current_day == "Sunday")):
    schedule.every().monday.at(monlist[1][9]).do(chrome(monlist[2][9]))
    schedule.every().tuesday.at(tuelist[1][9]).do(chrome(tuelist[2][9]))
    schedule.every().wednesday.at(wedlist[1][9]).do(chrome(wedlist[2][9]))
    schedule.every().monday.at(thulist[1][9]).do(chrome(thulist[2][9]))
    schedule.every().tuesday.at(frilist[1][9]).do(chrome(frilist[2][9]))
    schedule.every().wednesday.at(satlist[1][9]).do(chrome(satlist[2][9]))
    schedule.every().wednesday.at(sunlist[1][9]).do(chrome(sunlist[2][9]))
    while True:
        schedule.run_pending()
        time.sleep(1)




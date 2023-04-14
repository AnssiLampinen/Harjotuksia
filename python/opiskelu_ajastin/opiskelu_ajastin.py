import time
import datetime
import PySimpleGUI as sg
import studyin_time_data as std
import data_controll

local_time = time.localtime()
date = datetime.date(local_time[0], local_time[1], local_time[2]).isocalendar()

STUDY_TIME = 12
BREAK_TIME = 3
daily_goal = 3*60*60    # 3 hours
time_left = STUDY_TIME
time_text = "20:00"
current_activity = "Studying"

layout = [

    [sg.Text((current_activity + ": "), font=('Helvetica', 20), key="activity"), 
     sg.Text((time_text), font=('Helvetica', 20), key="time")],
    [sg.Text(("Studying done today: "), font=('Helvetica', 20) , key="1")],
    [sg.Text(("Studying goal per day: "), font=('Helvetica', 20) , key="2")],
    [sg.Text(("Mon   Tue   Wed   Thu   Fri   Sat   Sun"), font=('Helvetica', 20) , key="3")],
    [sg.Text((""), font=('Helvetica', 20) , key="4")],
    [sg.Exit(font=('Helvetica', 20) ,key="Exit"), 
     sg.Button("Plank", font=('Helvetica', 20) ,key="Plank")]
]

window = sg.Window("Timer", layout, size = (700, 400))

while True:
    event, values = window.read(timeout = 1000)
    
    if time_left:
        time_left -= 1
        mins, secs = divmod(time_left, 60)
        time_text = '{:02d}:{:02d}'.format(mins, secs)
        window["time"].update(time_text)
        window["activity"].update(current_activity + ": ")

    elif current_activity == "Studying":
        current_activity = "Break"
        time_left = BREAK_TIME
        event, values = window.read()

    elif current_activity == "Break":
        current_activity = "Studying"
        time_left = STUDY_TIME
        event, values = window.read()
        data_controll.modify_study_time(date[0], 14, date[2], STUDY_TIME)

    
    if event in (sg.WIN_CLOSED, "Exit"):
        break

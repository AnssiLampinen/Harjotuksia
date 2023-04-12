import time
import PySimpleGUI as sg

STUDY_TIME = 12
BREAK_TIME = 3
time_left = STUDY_TIME
time_text = "20:00"
current_activity = "Studying"

layout = [
    [sg.Text(current_activity, font=('Helvetica', 20), key = "activity")],
    [sg.Text(("Time left: "), font=('Helvetica', 20)), 
     sg.Text((time_text), font=('Helvetica', 20) , key="time")],
    [sg.Text((""), font=('Helvetica', 20) , key="1")],
    [sg.Text((""), font=('Helvetica', 20) , key="2")],
    [sg.Text((""), font=('Helvetica', 20) , key="3")],
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
        window["activity"].update(current_activity)

    elif current_activity == "Studying":
        current_activity = "Break"
        time_left = BREAK_TIME
        event, values = window.read()

    elif current_activity == "Break":
        current_activity = "Studying"
        time_left = STUDY_TIME
        event, values = window.read()
    
    if event in (sg.WIN_CLOSED, "Exit"):
        break
        
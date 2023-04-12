import PySimpleGUI as sg
import time

sg.theme('DarkAmber')   # Add a touch of color

time_in_secs = 10
timer = 10
current_activity = "Studying"
next_activity = "drawing"

# def update_timer(time_in_secs):
#     mins, secs = divmod(time_in_secs, 60)
#     timer = '{:02d}:{:02d}'.format(mins, secs)
#     print(timer, end = "\r")
#     time.sleep(1)
#     time_in_secs -= 1
#     return timer, time_in_secs

# All the stuff inside your window.
layout = [  [sg.Text(current_activity + " for:")],
            [sg.Text(timer)],
            [sg.Text("Next activity: " + next_activity)],
            [sg.Button('Ok'), sg.Button('Quit')] ]

# Create the Window
window = sg.Window('Window Title', layout, size=(600, 150))

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    timer -= 1
    time.sleep(1)

window.close()
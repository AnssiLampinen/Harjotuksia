import PySimpleGUI as sg
import time
timer = 10

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text(timer)],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout, size=(600, 150))
# Event Loop to process "events" and get the "values" of the inputs

while True:
    layout = [  [sg.Text(timer)],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
    window = sg.Window('Window Title', layout, size=(600, 150))
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    else:
        print(timer)
        timer -= 1
        time.sleep(1)

window.close()
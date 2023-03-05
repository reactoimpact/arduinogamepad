import serial
import vgamepad as vg
import re
import PySimpleGUI as sg

# ask user to setup what com port the Aurdino is connected to
layout = [  
            [sg.Text("Please Enter the com port of the Aurdino Eg. COM3")], 
            [ sg.InputText(), sg.Submit()]  
         ]

window = sg.Window('Com port Selection', layout) 

event, values = window.read()    
window.close()

ComPort = values[0]   

# check if com port is valid else throw an error
com = re.findall("COM\d+", ComPort)
if len(com) != 0:

    ser = serial.Serial(ComPort, 9600)
    gamepad = vg.VX360Gamepad()

    layout = [  
                [sg.Text("GamePad Program is running!")] 
            ]

    window = sg.Window('Running', layout) 

    

    while True:
        event, values = window.read(timeout=1)  
        if event == sg.WIN_CLOSED:
            break

        line = re.findall("[A-Z]'(\d+|-\d+)'", str(ser.readline()))
        if len(line) < 2:
            line = ["0", "0", "0"]
        gamepad.left_joystick(x_value=int(line[2]), y_value=0)
        if int(line[0]) == 0:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        if int(line[1]) == 0:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()
else:
    sg.popup("ComPort should be formated like COM3")
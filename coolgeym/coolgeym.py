import turtle
from turtle import Screen, showturtle, hideturtle
import tkinter

import sys
import winsound
import time

window = turtle.Screen()
window.title("Sean gaming")
tkinter_canvas = window.getcanvas()

obunga_Canvas = window.getcanvas()
# setting a variable "window" and making it a screen

Wd = 800
Hg = 800
window.setup(Wd, Hg)

#setup window screen to programmers choice of size

turtle.bgcolor('black')
window.bgpic("bgpic.gif")
# adding a pic to the window
# note it should be .gif or it wont work

power = 101
task_Quota = 0
anger = 0

toggle_State = True

# ----- functions -----

def press():
    if toggle_State == False:
        show()
        task_Label.pack_forget()

    elif toggle_State == True:
        hide()
        task_Label.pack()
        task_Progress()


def show():
    global toggle_State
    toggle_State = True
    tablet.hideturtle()
    winsound.PlaySound('tablet_Close.wav', winsound.SND_ASYNC)
    tkinter_canvas.after(1)
    anger = anger + 1

def hide():
    global toggle_State
    toggle_State = False
    tablet.showturtle()
    winsound.PlaySound('tablet_Open.wav', winsound.SND_ASYNC)

def lose():
    sys.exit()

# ----- tablet -----
turtle_Screen = Screen()

obunga = turtle.Turtle()
turtle_Screen.addshape('obunga.gif')
obunga.shape('obunga.gif')

tablet = turtle.Turtle()
turtle_Screen.addshape('tabletpic.gif')
tablet.shape('tabletpic.gif')
tablet.hideturtle()

tkinter_button = tkinter.Button(tkinter_canvas.master, text = "Tablet", command = press,height = 1,width = 10, font = ("Arial", 35))
tkinter_canvas.create_window(-10, Hg/3, window = tkinter_button)


# ----- power level -----

power_Level = tkinter.Label(tkinter_canvas.master, text = "Power Level: {} ".format(power), font = ("Arial", 15))
tkinter_canvas.create_window(-300, -350, window = power_Level)

def power_Level_Label():
    global power
    if power >= 1:
         power = power - 1
         power_Level.after(4000, power_Level_Label)
         power_Level.config(text = "Power Level: {} ".format(power))
         power_Level.update()

    elif power < 1:
        lose("L you lost")

power_Level_Label()


# ----- task -----


task_Label = tkinter.Label(tkinter_canvas.master, text = "progress: {}/100 ".format(task_Quota), font = ("Arial", 15))
tkinter_canvas.create_window(-1000, -1000, window = task_Label, state = "disabled")

def task_Progress():
    global task_Quota
    while toggle_State == False:
        if task_Quota <= 99:
            task_Quota = task_Quota + 1
            task_Label.config(text = "progress: {}/100 ".format(task_Quota))
            task_Label.after(500)
            task_Label.update()
        
# ----- mosnter -----

if anger > 10:
    lose()

turtle.done()

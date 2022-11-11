import turtle
# turtle is like pygame with less steps
import tkinter as tkinter
from tkinter import *
from tkinter import font
# tkinter is a simple GUI toolkit
import time

window = turtle.Screen()
#window.title("Sean gaming")
# setting a variable "window" and making it a screen

Wd = 800
Hg = 800
window.setup(Wd, Hg)
#setup window screen to programmers choice of size

window.bgpic("bgpic.gif")
# adding a pic to the window
# note it should be .gif or it wont work

def press():
    do_stuff()

def do_stuff():
    exit()
# basically we are making our own functions so when we call press or do_stuff its gonna call whats indented on it

tkinter_canvas = window.getcanvas()
tkinter_button = tkinter.Button(tkinter_canvas.master, text = "Tablet", command = press,height = 1,width = 10, font = ("Arial", 35))
tkinter_canvas.create_window(-10, Hg/3, window = tkinter_button)
# basically the button itself, we first tried to link up tkinter and turtle on the first line of this block then 
# made a button and created a window for it inside the turtle screen

power = 100

power_Level = tkinter.Label(tkinter_canvas.master, text = "Power Level: {} ".format(power), font = ("Arial", 15))
tkinter_canvas.create_window(-300, -350, window = power_Level)

def power_Level_Label():
    global power
    power = power - 1
    power_Level.config(text = "Power Level: {} ".format(power))

while power >= 1:
  power_Level_Label()

# from line 35 to line 43 is one of the hardest things i had to make that would be usually easy when using a game engine, so basically i declared a power variable that will
# control the power to have an end game option where when your power runs out meaning 0 you lose, so basically here i made the variable global because which for some reason
# dosent work if the variable is local(by default it is local). anyways moving on i made the label called power_level and made a function so i can just run it whenever i want to
# then the power_level.after(5000) is basically time.sleep(5) because tkinter dosent work when you use time.sleep(). then I update the screen with the new changes being the label


turtle.done()

#!/usr/bin/env python3

#import tkinter pkg, include widgets: Label, Tk
#Label: display text and bitmaps
#Tk: displays main window of application
from tkinter import Label, Tk
import time

#construct application window with title, set dimensions, & make it resizable
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry('500x200')
app_window.resizable(1,1)

#define the text font style, colors, and set border width
text_font = ("Boulder", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

#define the label variable and pass it the params defined above
label = Label(app_window, font = text_font, bg = background, fg = foreground, bd = border_width)
label.grid(row = 0, column = 1)

#set the digital clock to display {hour/min/sec} 
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

#invoke/initiate the digital clock
digital_clock()
app_window.mainloop()
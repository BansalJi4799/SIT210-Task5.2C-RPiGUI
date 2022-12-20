# YUVRAJ BANSAL
# 2110994799
# Task 5.2C

#  GUI LIbrary
from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
from gpiozero import LED
GPIO.setmode(GPIO.BCM)

#Initializing GPIO pins
red = LED(4)
blue = LED(14)
green = LED(15)

# Initializing GUI wwindow
win = Tk()
# Title for GUI Interface
win.title("GUI Interface")
win.geometry("250x180")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
uv = StringVar()

# Declaring functions for the functionality of the GUI Widgets
def ledRed():
    red.on()
    blue.off()
    green.off()
  
        
def ledBlue(): 
    red.off()
    blue.on()
    green.off()
    

def ledGreen():
    red.off()
    blue.off()
    green.on()
    

def allOn():
    red.on()
    blue.on()
    green.on()
    

def allOFF():
    red.off()
    blue.off()
    green.off()
       
# Exit button to destroy the window
def close():
    GPIO.cleanup()
    win.destroy()
    
# GUI Widgets
Label(win, text="Choose an option!!", font = myFont, padx = 14).pack()
Radiobutton(win, text="Red", font = myFont, command = ledRed, bg = 'red', height= 1, width = 27, bd = 3, variable = uv, value = "LED: Red").pack(anchor = "w")
Radiobutton(win, text="Blue", font = myFont, command = ledBlue, bg = 'blue', height= 1, width = 27, bd = 3, variable = uv, value = "LED: Blue").pack(anchor = "w")
Radiobutton(win, text="Green", font = myFont, command = ledGreen, bg = 'green', height= 1, width = 27, bd = 3, variable = uv, value = "LED: Green").pack(anchor = "w")
Radiobutton(win, text="All", font = myFont, command = allOn, bg = 'yellow', height= 1, width = 27, bd = 3, variable = uv, value = "LED: All").pack(anchor = "w")
Radiobutton(win, text="None", font = myFont, command = allOFF, bg = 'purple', height= 1, width = 27, bd = 3, variable = uv, value = "LED: None").pack(anchor = "w")
Button(win, text="Exit", font= myFont, command = close, bg='grey').pack(anchor = "w")

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

red = LED(4)
blue = LED(14)
green = LED(15)

win = Tk()
win.title("GUI Interface")
win.geometry("275x175")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

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

def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
Label(win, text="Choose an option!!").pack()
radio = Radiobutton(win, text="Red",command = ledRed, bg = 'red', height= 1, width = 25)
radio = Radiobutton(win, text="Blue",command = ledBlue, bg = 'blue', height= 1, width = 25)
radio = Radiobutton(win, text="Green",command = ledGreen, bg = 'green', height= 1, width = 25)
radio = Radiobutton(win, text="All",command = allOn, bg = 'yellow', height= 1, width = 25)
radio = Radiobutton(win, text="None",command = allOFF, bg = 'yellow', height= 1, width = 25)
Button(win, text="Exit", font= myFont, command = close, bg='grey')

win.protocol("WM_DELETE_WINDOW",close)
win.mainloop()
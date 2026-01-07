import time
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound

def beep():
     winsound.Beep(640,5000)

def current_time():
   totalSecounds = calendar.timegm(time.gmtime())
   currentSecound=totalSecounds%60
   if currentSecound < 10:
        currentSecound = "0"+str(currentSecound)


   totalMinutes= totalSecounds//60
   currentMinute=totalMinutes%60
   if currentMinute < 10:
        currentMinute = "0"+str(currentMinute)

   totalHours=totalMinutes//60
   currentHour=(totalHours%24)-6

   am_pm = ""
   if currentHour>=12:
        am_pm="PM"
   if currentHour==0:
        currentHour=currenthour+12
   else:
     am_pm="AM"
     if currentHour==0:
        currentHour=currenthour+12
   a=str(9)+":"+str(31)+":"+str(0)+"AM"

   timex=str(currentHour)+":"+str(currentMinute)+":"+str(currentSecound)+" "+am_pm
   if timex == a:
        beep()
   return timex
def show_time():
   time = current_time()
   txt.set(time)
   root.after(1000, show_time)

root = Tk()
# set window size
root.geometry("500x200")
root.configure(background='Green')

#font
root.after(1000, show_time)
fnt= font.Font(family='Hevetica',size=60,weight="bold")
txt = StringVar()

#display time and set up the colors

lbl=ttk.Label(root,textvariable=txt, font=fnt, foreground="Green",background="black")
lbl.place(relx=0.5, rely=0.5, anchor= CENTER)
#start

root.mainloop()
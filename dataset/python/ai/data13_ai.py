import time
from tkinter import Tk, StringVar, CENTER
from tkinter import ttk, font
import winsound

ALARM_TIME = "09:31:00 AM"

def beep():
    winsound.Beep(640, 5000)

def get_current_time() -> str:
    """Return the current local time as a formatted string."""
    local_time = time.localtime()
    return time.strftime("%I:%M:%S %p", local_time)

def show_time():
    current = get_current_time()
    txt.set(current)
    if current == ALARM_TIME:
        beep()
    root.after(1000, show_time)

# Tkinter GUI setup
root = Tk()
root.geometry("500x200")
root.configure(background='green')

fnt = font.Font(family='Helvetica', size=60, weight="bold")
txt = StringVar()

lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="green", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.after(1000, show_time)
root.mainloop()

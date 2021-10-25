import time
from tkinter import Tk
from tkinter import Label

root = Tk()
root.title("clock")


def present_time():
    display = time.strftime("%I:%M:%S %p")
    digi_clock.config(text=display)
    digi_clock.after(200,present_time)


digi_clock = Label(root,font=("arial",150),bg="black",fg="green")
digi_clock.pack()
present_time()
root.mainloop()

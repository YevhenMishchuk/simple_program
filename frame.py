from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Frame")
root.iconbitmap('@/home/marsy/Downloads/pumpkin.xbm')

frame=LabelFrame(root, text="Usefull frame", padx=20,pady=20)
frame.pack(padx=100,pady=100)

point=Button(frame, text="Simple button")
point2=Button(frame, text="Another button")
point.grid(row=0,column=0)
point2.grid(row=1,column=0)

root.mainloop()
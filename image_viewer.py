from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Sim Win")
root.iconbitmap('@/home/marsy/Downloads/pumpkin.xbm')


img_win1=ImageTk.PhotoImage(Image.open('/home/marsy/py_for_sci/exercises_23_07_2022_gui/images/1.png'))
img_win2=ImageTk.PhotoImage(Image.open('/home/marsy/py_for_sci/exercises_23_07_2022_gui/images/2.png'))
img_win3=ImageTk.PhotoImage(Image.open('/home/marsy/py_for_sci/exercises_23_07_2022_gui/images/3.png'))
img_win4=ImageTk.PhotoImage(Image.open('/home/marsy/py_for_sci/exercises_23_07_2022_gui/images/4.png'))
img_win5=ImageTk.PhotoImage(Image.open('/home/marsy/py_for_sci/exercises_23_07_2022_gui/images/5.png'))

img_list=[img_win1,img_win2,img_win3,img_win4,img_win5]


label_win=Label(image=img_win1)
label_win.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global label_win
    global button_forward
    global button_back

    label_win.grid_forget()
    label_win=Label(image=img_list[image_number-1])
    
    button_forward=Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back=Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number==5:
        button_forward=Button(root, text=">>", state=DISABLED)

    label_win.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)


def back(image_number):
    global label_win
    global button_forward
    global button_back

    label_win.grid_forget()
    label_win=Label(image=img_list[image_number-1])
    
    button_forward=Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back=Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number==1:
        button_back=Button(root, text="<<", state=DISABLED)

    label_win.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)



button_back=Button(root, text="<<", command=back, state=DISABLED)
button_quit=Button(root, text="Exit Program", command=root.quit)
button_forward=Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()
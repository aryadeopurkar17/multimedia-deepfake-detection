
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo

root=tk.Tk()

root.title("Deep Fake Detection")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

# bg = Image.open(r"/y9.jpg")
# bg.resize((1366,500),Image.ANTIALIAS)
# print(w,h)
# bg_img = ImageTk.PhotoImage(bg)
# bg_lbl = tk.Label(root,image=bg_img)
# bg_lbl.place(x=0,y=93)
# #, relwidth=1, relheight=1)

video_label =tk.Label(root)
video_label.pack()
# read video to display on label
player = tkvideo("C.mp4", video_label,loop = 1, size = (w, h))
player.play()
 
##w = tk.Label(root, text="Agriculture Pest Detection System",width=110,background="white",foreground="black",height=2,font=("Times new roman",19,"bold"))
##w.place(x=0,y=10)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#800517")


from tkinter import messagebox as ms


def st ():
    from subprocess import call
    call(["python","GUI_main.py"])



d2=tk.Button(root,text="Start",command=st,width=15,height=1,bd=0,background="White",foreground="black",font=("times new roman",17,"bold"))
d2.place(x=600,y=580)


##wlcm=tk.Label(root,text="...... WELCOME TO Agri Pest \n Detection System ......",width=30, height=4, background="white",foreground="Green",font=("Times new roman",19,"bold"))
##wlcm.place(x=490,y=300)







# d3=tk.Button(root,text="REGISTER",command=Register,width=20,height=2,bd=0,background="#800517",foreground="white",font=("times new roman",17,"bold"))
# d3.place(x=100,y=0)



root.mainloop()

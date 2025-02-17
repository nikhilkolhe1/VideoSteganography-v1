# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:36:00 2023

@author: admin
"""

from tkinter import *
import tkinter
import tkinter as tk

from tkinter import messagebox as ms
import sqlite3
from PIL import ImageTk,Image
import re

root=tk.Tk()

root.configure(background="white")

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

root.title("Home page")

image2=Image.open("Air1.jpg")
image2=image2.resize((1600,800),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image

background_label.place(x=0,y=0)

frame=Frame(root,bg="white")
frame.place(x=0,y=0,height=30,width=1700)

label =Label(root, text="VIDEO STEGANOGRAPHY", font=("times new roman", 31), bg="gray80",fg="black")
label.place(x=0, y=0,width=1590)

def reg():
    from subprocess import call
    call(["python","home.py"])
    
    
def log1():
        from subprocess import call
        call(["python","features.py"])
        
def log2():
    from subprocess import call
    call(["python","vid_steg.py"]) 
    

    


########################################## ADD BUTTON ###############################################################
registration_button = tk.Button(root, text="HOME PAGE",command=reg,font=("Helvetica", 18, "bold"), bg="pink", fg="green",bd=4)
registration_button.place(x=450, y=300, height=40, width=200)


login_button = tk.Button(root, text="Features",command=log1,font=("Helvetica", 18, "bold"), bg="pink", fg="green",bd=4)
login_button.place(x=800, y=300, height=40, width=300)

login_button = tk.Button(root, text="video stegno",command=log2,font=("Helvetica", 18, "bold"), bg="pink", fg="green",bd=4)
login_button.place(x=550, y=400, height=40, width=400)





exit_button = tk.Button(root, text="Exit", font=("Helvetica", 18, "bold"), bg="pink", fg="red",command=root.quit)
exit_button.place(x=680, y=530, height=35, width=142)

root.mainloop()
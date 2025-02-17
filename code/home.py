# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:51:56 2023

@author: admin
"""

import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()



#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))






Height = tk.IntVar()
Weight = tk.IntVar()

def main():
    h = Height.get()
    w = Weight.get()
    

image2 = Image.open('img2.jpg')
image2 = image2.resize((1600, 800), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



lbl = tk.Label(root, text="Welcome to HOME PAGE", font=('Lucida Sans Unicode', 40,' bold ',), height=1, width=50,bg="#8B0A50",fg="white")
lbl.place(x=0, y=3)

# framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=500, height=250, bd=5, font=('times', 14, ' bold '),bg="pink")
# framed.grid(row=0, column=0, sticky='nw')
# framed.place(x=450, y=300)


# logolbl=tk.Label(LabelFrame,bd=0).grid(row=0,columnspan=2,pady=20)
        
# lbluser=tk.Label(LabelFrame,text="Username",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
# txtuser=tk.Entry(LabelFrame,bd=5,textvariable=username,font=("",15),bg="white")
# txtuser.grid(row=1,column=1,padx=20)



        
Login_frame=tk.Frame(root,bg="#DB7093")
Login_frame.place(x=100,y=200)
        
logolbl=tk.Label(Login_frame,bd=0).grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(Login_frame,text="About Us \n Video steganography is the process of hiding secret information inside videos.\n The secret information can be any media like text, audio, images, video, and binary \n file and the carrier video can be raw/compressed in any format",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image



         


root.mainloop()
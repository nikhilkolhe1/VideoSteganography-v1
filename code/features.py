# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:57:12 2023

@author: admin
"""

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
    

image2 = Image.open('pxfuel (8).jpg')
image2 = image2.resize((1600, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



lbl = tk.Label(root, text="Features of video steganography", font=('Lucida Sans Unicode', 40,' bold ',), height=1, width=50,bg="black",fg="white")
lbl.place(x=0, y=3)





        
Login_frame=tk.Frame(root)
Login_frame.place(x=190,y=120)     
lbluser=tk.Label(Login_frame,text=" video steganography: \n Video steganography approach enables hiding chunks of secret information ",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
#++++++++++++++++++++++++++++++++++++++++++++++++



Login_frame=tk.Frame(root)
Login_frame.place(x=350,y=250)   
lbluser=tk.Label(Login_frame,text="Real-Time Feedback: \n  The process of hiding secret information inside videos ",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
#++++++++++++++++++++++++++++++++++++++++++++




Login_frame=tk.Frame(root)
Login_frame.place(x=200,y=400)      
lbluser=tk.Label(Login_frame,text="Educational Mode: \n Steganography, the practice of hiding information, has been around for centuries. More recently, \n it has been associated with some forms of cyber attacks",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
#++++++++++++++++++++++++++++++++++++++++++++


Login_frame=tk.Frame(root)
Login_frame.place(x=100,y=550)
lbluser=tk.Label(Login_frame,text="Security Measures: \n his technique embeds important data or secret messages into cover media to prevent unauthorized access ",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)



         


root.mainloop()
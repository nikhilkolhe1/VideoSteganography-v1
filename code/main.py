

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("VIDEO STEGANOGRAPHY")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('img5.jpg')
image2 = image2.resize((1600, 850), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

label_l1 = tk.Label(root, text="VIDEO STEGANOGRAPHY",font=("Times New Roman", 35, 'bold'),
                    background="#152238", fg="white", width=60, height=2)
label_l1.place(x=0, y=0)




label=tk.Label(root,text='''
               Since human visual system are less sensitive to the small 
               changes of digital medias, especially for digital video, 
               video steganography is a technique which hides message into 
               a video and conceals the fact of the transmission.
               '''
               ,font=("Calibri",12),bg='pink',
               
               fg="black")
label.place(x=500,y=150)

label=tk.Label(root,text='''
               Video steganography is the process of hiding secret information 
               inside videos. The secret information can be any media like text, 
               audio, images, video, and binary file and the carrier video can 
               be raw/compressed in any format.
               '''
               ,font=("Calibri",12),bg='pink',
               
               fg="black")
label.place(x=600,y=350)


label=tk.Label(root,text='''
               Secret messages can be introduced into the least significant 
               bits in an image and then hidden. A steganography tool can be 
               used to camouflage the secret message in the least significant 
               bits but it can introduce a random area that is too perfect.
               '''
               ,font=("Calibri",12),bg='pink',
               
               fg="black")
label.place(x=700,y=550)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=100, y=160)

button2 = tk.Button(root, text="Registration",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button2.place(x=100, y=240)

button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button3.place(x=100, y=320)

root.mainloop()
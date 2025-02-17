# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:46:17 2023

@author: COMPUTER
"""
import numpy as np
import pandas as pand
import os
import cv2
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter import messagebox as ms
from tkinter.filedialog import askopenfilename
global fn
global vid
global frame_
frame_=""
vid=""

fn=""


root = tk.Tk()
root.configure(background="pink")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("main")

current_path = str(os.path.dirname(os.path.realpath('__file__')))

basepath=current_path  + "\\" 

frame_no = tk.StringVar()
frame_no2 = tk.StringVar()
encode_text = tk.StringVar()
key1 = tk.StringVar()
key2 = tk.StringVar()

label_l1 = tk.Label(root, text="VIDEO STEGANOGRAPHY", font=("Times New Roman", 35, 'bold'),
                    background="#009ACD", fg="black", width=60, height=2)
label_l1.place(x=0, y=0)

frame_display = tk.LabelFrame(root, text=" --Display-- ", width=1200,
                              height=630, bd=5, font=('times', 14, ' bold '), bg="lightblue4")
frame_display.grid(row=0, column=0, sticky='nw')
frame_display.place(x=400, y=150)


image2=Image.open("v1.webp")
image2=image2.resize((1200,800),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label=tk.Label(frame_display,image=background_image)

background_label.image=background_image

background_label.place(x=0,y=0)


def msgtobinary(msg):
    if type(msg) == str:
        result= ''.join([ format(ord(i), "08b") for i in msg ])
    
    elif type(msg) == bytes or type(msg) == np.ndarray:
        result= [ format(i, "08b") for i in msg ]
    
    elif type(msg) == int or type(msg) == np.uint8:
        result=format(msg, "08b")

    else:
        raise TypeError("Input type is not supported in this function")
    
    return result

def KSA(key):
    key_length = len(key)
    S=list(range(256)) 
    j=0
    for i in range(256):
        j=(j+S[i]+key[i % key_length]) % 256
        S[i],S[j]=S[j],S[i]
    return S

def PRGA(S,n):
    i=0
    j=0
    key=[]
    while n>0:
        n=n-1
        i=(i+1)%256
        j=(j+S[i])%256
        S[i],S[j]=S[j],S[i]
        K=S[(S[i]+S[j])%256]
        key.append(K)
    return key


def preparing_key_array(s):
    return [ord(c) for c in s]


def encryption(plaintext):
    
    key=key1.get()
    print("key",key)
    key=preparing_key_array(key)

    S=KSA(key)

    keystream=np.array(PRGA(S,len(plaintext)))
    plaintext=np.array([ord(i) for i in plaintext])

    cipher=keystream^plaintext
    ctext=''
    for c in cipher:
        ctext=ctext+chr(c)
    return ctext

def decryption(ciphertext):
    
    key=key2.get()
    print("key",key)
    key=preparing_key_array(key)

    S=KSA(key)

    keystream=np.array(PRGA(S,len(ciphertext)))
    ciphertext=np.array([ord(i) for i in ciphertext])

    decoded=keystream^ciphertext
    dtext=''
    for c in decoded:
        dtext=dtext+chr(c)
        print(dtext)
    return dtext
    
def embed(frame):
    data=encode_text.get()
    print("Data to encode",data)
    data=encryption(data)
    print("The encrypted data is : ",data)
    if (len(data) == 0): 
        raise ValueError('Data entered to be encoded is empty')

    data +='*^*^*'
    
    binary_data=msgtobinary(data)
    length_data = len(binary_data)
    
    index_data = 0
    
    for i in frame:
        for pixel in i:
            r, g, b = msgtobinary(pixel)
            if index_data < length_data:
                pixel[0] = int(r[:-1] + binary_data[index_data], 2) 
                index_data += 1
            if index_data < length_data:
                pixel[1] = int(g[:-1] + binary_data[index_data], 2) 
                index_data += 1
            if index_data < length_data:
                pixel[2] = int(b[:-1] + binary_data[index_data], 2) 
                index_data += 1
            if index_data >= length_data:
                break
        return frame    
  
def extract(frame):
    print("hello",frame)
    data_binary = ""
    final_decoded_msg = ""
    for i in frame:
        print(1)
        for pixel in i:
            print(2)
            r, g, b = msgtobinary(pixel) 
            data_binary += r[-1]  
            data_binary += g[-1]  
            data_binary += b[-1]  
            total_bytes = [ data_binary[i: i+8] for i in range(0, len(data_binary), 8) ]
            print("total_bytes",total_bytes)
            decoded_data = ""
            for byte in total_bytes:
                #print(3)
               # print("byte",byte)
                decoded_data += chr(int(byte, 2))
                #print("decoded_data",decoded_data)
                if decoded_data[-5:] == "*^*^*": 
                  #  print(4)
                    for i in range(0,len(decoded_data)-5):
                   #     print(5)
                        final_decoded_msg += decoded_data[i]
                    final_decoded_msg = decryption(final_decoded_msg)
                   #print("\n\nThe Encoded data which was hidden in the Video was :--\n",final_decoded_msg)
                    # result1="The Encoded data which was hidden in the Video was :--"+final_decoded_msg
                    # ms.showinfo("Message", result1)
                    # return 
                    #if v[0]==0:
                        
                   

                    print("\n\nThe Encoded data which was hidden in the Video was :--\n",final_decoded_msg)
                    yes = tk.Label(root,text="The Encoded data which was hidden in the Video was ",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
                    yes.place(x=250,y=500)
                       
                
                

def enc_main(vid):
    cap=cv2.VideoCapture(vid)
    vidcap = cv2.VideoCapture(vid)    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    frame_width = int(vidcap.get(3))
    frame_height = int(vidcap.get(4))

    size = (frame_width, frame_height)
    out = cv2.VideoWriter('stego.mp4',fourcc, 25.0, size)
    max_frame=0;
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        max_frame+=1
    cap.release()
    print("Total number of Frame in selected Video :",max_frame)
    label_l1 = tk.Label(frame_display, text="Total number of Frame in selected Video :" + str(max_frame), font=("Times New Roman", 15, 'bold'),
                        background="#009ACD", fg="black", width=50, height=2)
    label_l1.place(x=100, y=50)
    #print("Enter the frame number where you want to embed data : ")
    label_l1 = tk.Label(frame_display, text="Enter the frame number where you want to embed data : ", font=("Times New Roman", 15, 'bold'),
                        background="#009ACD", fg="black", width=50, height=2)
    label_l1.place(x=100, y=150)
    t2 = tk.Entry(frame_display, textvar=frame_no, width=20, font=('', 15))
    t2.place(x=800, y=150)
    label_l1 = tk.Label(frame_display, text="Enter the data to be Encoded in Video : ", font=("Times New Roman", 15, 'bold'),
                        background="black", fg="white", width=50, height=2)
    label_l1.place(x=100, y=250)
    t2 = tk.Entry(frame_display, textvar=encode_text, width=20, font=('', 15))
    t2.place(x=800, y=250)
    label_l1 = tk.Label(frame_display, text="Enter the Key : ", font=("Times New Roman", 15, 'bold'),
                        background="black", fg="white", width=50, height=2)
    label_l1.place(x=100, y=350)
    t2 = tk.Entry(frame_display, textvar=key1, width=20, font=('', 15))
    t2.place(x=800, y=350)
    def enc_sub():
        global frame_
        vidcap = cv2.VideoCapture(vid)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        frame_width = int(vidcap.get(3))
        frame_height = int(vidcap.get(4))
    
        size = (frame_width, frame_height)
        out = cv2.VideoWriter('stego.mp4', fourcc, 25.0, size)
        max_frame = 0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            max_frame += 1
        cap.release()
        n=frame_no.get()
        print("frame no.",n)
        n=int(n)
        frame_number = 0
        
        while(vidcap.isOpened()):
            frame_number += 1
            ret, frame = vidcap.read()
            if ret == False:
                break
            if frame_number == n:    
                change_frame_with = embed(frame)
                frame_ = change_frame_with
                frame = change_frame_with
            out.write(frame)
        
        print("\nEncoded the data successfully in the video file.")
        ms.showinfo("Message", "Encoded the data successfully in the video file.")
        
        return frame_    
    
    
    btn = tk.Button(frame_display, text="Submit", bg="red", font=("", 20), fg="white", width=9, height=1, command=enc_sub)
    btn.place(x=500, y=450)
    
def main():
    

    global fn
    

    #fn = ""
    fileName = askopenfilename(initialdir='/dataset', title='Select image',
                               filetypes=[("all files", "*.*")])

    videopath = fileName
    print(fileName)
    #fn = fileName
    fn = fileName
    Sel_F = fileName.split('/').pop()
    Sel_F = Sel_F.split('.').pop(1)

    if Sel_F != 'mp4':
        print("Select Video .mp4 File!!!!!!")
    else:
        enc_main(fn)

        
def dec_main():
    fileName = askopenfilename(initialdir='/dataset', title='Select image',
                               filetypes=[("all files", "*.*")])

    videopath = fileName
    print(fileName)
    #fn = fileName
    fn = fileName
    Sel_F = fileName.split('/').pop()
    Sel_F = Sel_F.split('.').pop(1)

    # if Sel_F != 'mp4':
    #     print("Select Video .mp4 File!!!!!!")
    # else:
        #enc_main(fn)
    cap = cv2.VideoCapture(fn)
    max_frame1=0;
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        max_frame1+=1
    print("Total number of Frame in selected Video :",max_frame1)
    print("Enter the secret frame number from where you want to extract data")
    frame_display = tk.LabelFrame(root, text=" --Display-- ", width=1100,
                                  height=630, bd=5, font=('times', 14, ' bold '), bg="lightblue4")
    frame_display.grid(row=0, column=0, sticky='nw')
    frame_display.place(x=400, y=150)
    image2=Image.open("v1.webp")
    image2=image2.resize((1200,800),Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label=tk.Label(frame_display,image=background_image)

    background_label.image=background_image

    background_label.place(x=0,y=0)


    label_l1 = tk.Label(frame_display, text="Total number of Frame in selected Video :" + str(max_frame1), font=("Times New Roman", 15, 'bold'),
                        background="#009ACD", fg="black", width=50, height=2)
    label_l1.place(x=100, y=50)

    label_l1 = tk.Label(frame_display, text="Enter the secret frame number from where you want to extract data", font=("Times New Roman", 15, 'bold'),
                        background="#009ACD", fg="black", width=50, height=2)
    label_l1.place(x=100, y=150)
    t2 = tk.Entry(frame_display, textvar=frame_no2, width=20, font=('', 15))
    t2.place(x=800, y=150)
    label_l1 = tk.Label(frame_display, text="Enter the Key : ", font=("Times New Roman", 15, 'bold'),
                        background="black", fg="white", width=50, height=2)
    label_l1.place(x=100, y=250)
    t2 = tk.Entry(frame_display, textvar=key2, width=20, font=('', 15))
    t2.place(x=800, y=250)
    
    def dec_sub():
        global frame_
        print(frame_)
       
        n1=frame_no2.get()
        print("Frame no",n1)
        n1=int(n1)
        vidcap = cv2.VideoCapture('stego.mp4')
        frame_number = 0
        while(vidcap.isOpened()):
            frame_number += 1
            ret, frame = vidcap.read()
            if ret == False:
                print("fail")
                break
            if frame_number == n1:
                print("pass")
                extract(frame_)
                
                return  
    btn = tk.Button(frame_display, text="Submit", bg="red", font=("", 20), fg="white", width=9, height=1, command=dec_sub)
    btn.place(x=500, y=350)
      
def window():
    root.destroy()


button1 = tk.Button(root, text="Upload Video", command=main, width=14,
                    height=1, font=('times', 20, ' bold '), bg="#8B0A50", fg="white")
button1.place(x=20, y=200)

button3 = tk.Button(root, text="Decode", command=dec_main, width=14,
                    height=1, font=('times', 20, ' bold '), bg="#8B0A50", fg="white")
button3.place(x=20, y=400)



button3 = tk.Button(root, text="EXIT", command=window, width=14,
                    height=1, font=('times', 20, ' bold '), bg="red", fg="black")
button3.place(x=20, y=500)

# if __name__ == "__main__":
#     main()
root.mainloop()

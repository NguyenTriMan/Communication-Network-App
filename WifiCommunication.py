import tkinter as tk
from tkinter import *
from tkinter import font
import tkinter.messagebox
import smtplib,ssl
import serial
import os
import pygame
import socket

host = '192.168.43.124'  # Host ip
port = 1234          
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

root = tk.Tk()
root.title('Communication')
root.geometry('900x600')
#play music
pygame.mixer.init()
pygame.mixer.music.load("ikon.mp3")
pygame.mixer.music.play()


def send():
    conn, addr = s.accept()
    print('Connected by', addr) 
    global msg
    # global msgReserve
    msg = entrySend.get()
    # msgReserve = msg[::-1]
    conn.send(bytes(msg,"utf-8"))


def receive():
    global msg
    entryReceive.delete(0,20)
    entryReceive.insert(ANCHOR,msg)

#background
background = tk.PhotoImage(file = 'bglandscape.png')
background_label = tk.Label(root, image = background)
background_label.place(relheight = '1', relwidth = '1')
# GUI
labelSend = tk.Label(root, text = 'Send here',font = ('Times New Roman bold italic',13 ),bg = '#FDBDDC' , fg = 'black')
labelReceive = tk.Label(root, text = 'Receive here',font = ('Times New Roman bold italic',13 ),bg = '#FDBDDC' , fg = 'black')
labelPort = tk.Label(root, text = 'Port name',font = ('Times New Roman bold italic',13 ),bg = '#FDBDDC' , fg = 'black')
labelBaud = tk.Label(root, text = 'Baud Rate',font = ('Times New Roman bold italic',13 ),bg = '#FDBDDC' , fg = 'black')
entrySend = tk.Entry(root,font = ('Times New Roman italic',13))
entryReceive = tk.Entry(root,font = ('Times New Roman italic',13))
buttonSend = tk.Button(root,text = 'Send',font = ('Times New Roman bold',15),fg = 'red',bg = 'blue', command = send)
buttonReceive = tk.Button(root,text = 'Receive',font = ('Times New Roman bold',15),fg = 'red',bg = 'blue', command = receive)
buttonOpenport = tk.Button(root,text = 'Connect',font = ('Times New Roman bold',15),fg = 'red',bg = 'blue')
buttonCloseport = tk.Button(root,text = 'Disconnect',font = ('Times New Roman bold',15),fg = 'red',bg = 'blue')
#create list
listPort = tk.Listbox(root)
for i in range (1,11):
    listPort.insert(i,'com%d' %i)

listbaud = tk.Listbox(root)
listbaud.insert(1,'4800')
listbaud.insert(2,'9600')
listbaud.insert(3,'115200')


# position
labelSend.place(relx = '0.1',rely = '0.3',relheight = '0.05' , relwidth = '0.1')
labelReceive.place(relx = '0.5',rely = '0.3',relheight = '0.05' , relwidth = '0.103')
labelPort.place(relx = '0.2',rely = '0.05',relheight = '0.05' , relwidth = '0.09')
labelBaud.place(relx = '0.5',rely = '0.05',relheight = '0.05' , relwidth = '0.09')

entrySend.place(relx = '0.1',rely = '0.4',relheight = '0.3' , relwidth = '0.3')
entryReceive.place(relx = '0.5',rely = '0.4',relheight = '0.3' , relwidth = '0.3')

buttonSend.place(relx = '0.1',rely = '0.7',relheight = '0.05' , relwidth = '0.09')
buttonReceive.place(relx = '0.5',rely = '0.7',relheight = '0.05' , relwidth = '0.09')
buttonOpenport.place(relx = '0.8',rely = '0.2',relheight = '0.05' , relwidth = '0.11')
buttonCloseport.place(relx = '0.8',rely = '0.3',relheight = '0.05' , relwidth = '0.11')

listPort.place(relx = '0.2',rely = '0.1',relheight = '0.06' , relwidth = '0.09')
listbaud.place(relx = '0.5',rely = '0.1',relheight = '0.06' , relwidth = '0.09')


root.mainloop()
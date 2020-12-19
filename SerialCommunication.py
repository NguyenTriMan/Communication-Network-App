import tkinter as tk
from tkinter import *
from tkinter import font
import tkinter.messagebox
import smtplib,ssl
import serial
import os
import pygame


root = tk.Tk()
root.title('Communicate serial')
root.geometry('900x600')
printer = serial.Serial()

pygame.mixer.init()
pygame.mixer.music.load("ikon.mp3")
pygame.mixer.music.play()

def openPort():
    global printer
    A = listPort.get(ANCHOR)
    B = listbaud.get(ANCHOR)
    printer = serial.Serial(A,B)
    print(A ,B)

def closePort():
    global printer
    printer.close()


def send():
    global printer
    #get message in box entrySend
    message = entrySend.get()
    printer.write(message.encode('utf8'))

def receive():
    global printer
    read = printer.read(size=15)
    entryReceive.delete(0,20)
    entryReceive.insert(ANCHOR,read)

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
buttonOpenport = tk.Button(root,text = 'Connect',font = ('Times New Roman bold',15),fg = 'red',bg = 'blue', command = openPort)
buttonCloseport = tk.Button(root,text = 'Disconnect',font = ('Times New Roman bold',15),fg = 'red',bg = 'blue', command = closePort)

#add list port
listPort = tk.Listbox(root)
for i in range (1,11):
    listPort.insert(i,'com%d' %i)

#add list baud rate
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

listPort.place(relx = '0.2',rely = '0.1',relheight = '0.1' , relwidth = '0.09')
listbaud.place(relx = '0.5',rely = '0.1',relheight = '0.1' , relwidth = '0.09')


root.mainloop()
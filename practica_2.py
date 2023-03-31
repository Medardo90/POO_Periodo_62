# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 00:26:39 2023

@author: Patricio Haro
"""
# import tkinter as tk
# from tkinter import ttk
# from tkinter import*
# from PIL import ImageTk, Image

from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk

raiz= tk.Tk()
raiz.title("Nueva_Practica_POO")
raiz.geometry("750x550")
raiz.config(bg="silver")
raiz.resizable(0,0)

img= Image.open("pokemon (1).png") 
img= img.resize((140, 120), Image.ANTIALIAS) 
img= ImageTk.PhotoImage(img)
label_ing = tk.Label(raiz, image = img)
label_ing.image = img
label_ing.place(x=40, y=40)

# cuadro = Entry(raiz, width = 12)
# cuadro.insert(0, "Precioname")
# cuadro.place( x=210, y=50)

cuadro = tk.Button(raiz, text = "Precioname",width = 12, bg ="silver" )
cuadro.place( x=210, y=50)

entry = tk.Entry(raiz, bg= "black", fg= "white", width=20)
entry.insert(0, "Username")
entry.place(x= 40, y=200)

entry1 = tk.Entry(raiz, bg= "black", fg= "white", width=20, show = "*")
entry1.place(x= 40, y=235)

listabox = tk.Listbox(raiz)
listabox.insert(0, "Patricio")
listabox.insert(1, "Rosendo")
listabox.insert(2, "Pilar")
listabox.insert(3, "Zenaida")
listabox.insert(4, "MIkaela")
listabox.insert(5, "Jefferson")
listabox.insert(6, "Jhony")
listabox.insert(7, "Ariel")
listabox.insert(8, "Nicolas")
listabox.insert(9, "Guido")
listabox.place(x= 40, y=320, width=150, height=120)
lisscroll = ttk.Scrollbar(raiz, orient=tk.VERTICAL, command=listabox.yview)
listabox.config(bg="silver", fg= "purple",yscrollcommand=lisscroll.set,borderwidth="5",)
lisscroll.place(x=190, y= 320, height=120)

frame = tk.Frame(raiz, background = "grey", width= 400, height= 250)
frame.place(x= 300, y= 250)

img2= Image.open("paisaje.png") 
img2= img2.resize((100, 80), Image.ANTIALIAS) 
img2= ImageTk.PhotoImage(img2)
label_img = tk.Label(frame, image = img2)
label_img.image = img2
label_img.place(x=220, y=120)

cuadro1 = tk.Button(frame, text = "Back",width = 4, bg ="silver" )
cuadro1.place( x=340, y=170)

entry1= tk.Entry(frame, bg= "black", fg= "white", width=22)
entry1.insert(0, "Username")
entry1.place(x= 180, y=20)

entry2= tk.Entry(frame, bg= "black", fg= "white", width=22)
entry2.insert(0, "Username")
entry2.place(x= 180, y=45)

texto = tk.Label(frame, text= "Slider", bg= "grey")
texto.place(x=40, y= 20)
texto1 = tk.Label(frame, text= "RangeSlider",bg= "grey")
texto1.place(x=40, y= 45)

lbcheck = tk.IntVar()
checkboton = tk.Checkbutton(frame, text="Checkbox",variable= lbcheck , bg= "grey")
checkboton.place(x= 40 , y= 120)

# labelcheck = tk.Label(frame, text="Checkbox", bg="grey")
# labelcheck.place(x=65, y= 80)
# checkboton = tk.Checkbutton(frame, bg= "grey")
# checkboton.place(x= 40 , y= 80)

radioboton = tk.IntVar()
radioboton1 = tk.Radiobutton(frame, text="Radiobutton", variable= radioboton, value = 1, bg= "grey")
radioboton1.place(x= 40, y= 150) 

raiz.mainloop()
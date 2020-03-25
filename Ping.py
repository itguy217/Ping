# -*- coding: utf-8 -*-
"""
This program is desinged to ping an ip address of your choseing.
The pragram makes use of a timer to reset the label.
This is the first ideration of this program that I made so please let me know 
if there is anything I should improve.
@author: Chris Thummel
"""
import threading 
import os
from tkinter import *

root = Tk()
root.title('Ping')
root.geometry("200x100")
root.configure(bg='white')

# The pinging function 
def ping ():
    x = e.get()
    response = os.system("ping -n 1 " + x)# This line is what dose the pinging.
    
    #Output if  there is a response.
    if response == 0:
        label_result.config(text= str(x)+  ' is up!')
        e.delete(0, END)
        timer = threading.Timer(5.0, Restart)# Timer setting 
        timer.start() # Activates timer.
        # This is if there is no response.
    else:
        label_result.config(text= str(x)+  ' is down!')
        e.delete(0, END)
        timer = threading.Timer(5.0, Restart)
        timer.start()
        
label_result = Label(root,  text ='Pick an IP you would like to ping.', bg = 'white' )
label_result.pack()
e = Entry(root, width=20, borderwidth=5)
e.pack()
button_set = Button(root, text = 'Ping', bg = 'blue', fg = 'yellow', activebackground = "gray63", padx=12, pady=2, command = ping ).pack()

# Changes label when the timer reaches 0
def Restart():
    label_result.config(text=' Pick an IP you would like to ping.')
  
root.mainloop()

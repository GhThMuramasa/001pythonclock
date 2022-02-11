from datetime import date, datetime
from time import strftime, time
from tkinter import *
from tkinter.font import Font
from turtle import bgcolor

# 001 tkinter initiate code
root= Tk()
root.title('. . . C L O C K . . .')
root.config(bg='black')
root.iconbitmap('images/icon.ico')
root.state('zoomed') # to maximize window
root.config(menu=None) # hide menu bar
root.wm_attributes('-fullscreen','True') # กำหนดให้ไม่ต้องแสดง title bar 

# 002 tkinter general display setting -- Font, Background 
fgcolor = 'white'
bgcolor = 'black'
fontsize = 300
timfontBig = Font(family='DS-Digital',size = fontsize, weight='bold')

# 003  Label Position
# Findout size of windows
screen_width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenheight()

ypos = (screen_height-fontsize)/2

lblTime = Label(root, foreground=fgcolor, bg= bgcolor, font=timfontBig)



# 004 SET TIME
def time():
    strTime = strftime('%H:%M:%S')
    lblTime.config(text=f'{strTime}')
    lblTime.pack(pady=ypos)
    lblTime.after(1000,time)

time()


root.mainloop()
from tkinter import *
from PIL import Image,ImageTk
from gtts import gTTS
from playsound import playsound

w=Tk()
w.geometry("300x350")
w.resizable(0,0)


Msg=StringVar()
def Text_to_speech():
    Message = e1.get()
    speech=gTTS(text=Message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')

def Exit():
    w.destroy()

def Reset():
    Msg.set("")


load=Image.open('image.png')
render=ImageTk.PhotoImage(load)
img=Label(w,image=render)
img.place(x=0,y=0)

l1=Label(w,text="Text  To  Speech  Converter",font=("Cooper Black",15))
l1.grid()

l2=Label(w,text="Enter Text :-",font=("Cooper Black",15))
l2.grid(pady="30",sticky="W")

e1=Entry(w,font=("Cooper Black",15),textvariable=Msg)
e1.grid()

b1=Button(w,text="Play",font=("Cooper Black",15),command=Text_to_speech)
b1.place(x=20,y=180)
b2=Button(w,text="Exit",font=("Cooper Black",15),command=Exit)
b2.place(x=110,y=180)
b3=Button(w,text="Reset",font=("Cooper Black",15),command=Reset)
b3.place(x=190,y=180)

w.mainloop()

from datetime import datetime
from tkinter import *

from PIL import Image, ImageTk
from gtts import gTTS
from playsound import playsound

frame = Tk()
frame.geometry("300x350")
frame.resizable(0, 0)

message = StringVar()


def get_and_save() -> None:
    fieldstring = str(ttsinputfield.get()).strip()
    if not fieldstring:
        print("Input field cannot be empty!")
        reset_field()
        return

    speech = gTTS(text=fieldstring)
    timenow = str(datetime.utcnow()).replace(':', '-').replace(' ', '-')

    filepath = f'resources/output-{timenow[: timenow.index(".")]}.mp3'
    speech.save(filepath)
    playsound(filepath)


def exit_app() -> None:
    frame.destroy()


def reset_field() -> None:
    message.set("")


load = Image.open('resources/background.png')
render = ImageTk.PhotoImage(load)
bglabel = Label(frame, image=render)
bglabel.place(x=0, y=0)

headerlabel = Label(frame, text="Text  To  Speech  Converter", font=("Cooper Black", 15))
headerlabel.grid()

inputfieldlabel = Label(frame, text="Enter Text:", font=("Cooper Black", 15))
inputfieldlabel.grid(pady="30", sticky="W")

ttsinputfield = Entry(frame, font=("Cooper Black", 15), textvariable=message)
ttsinputfield.grid()

playbutton = Button(frame, text="Play", font=("Cooper Black", 15), command=get_and_save)
playbutton.place(x=20, y=180)

exitbutton = Button(frame, text="Exit", font=("Cooper Black", 15), command=exit_app)
exitbutton.place(x=110, y=180)

resetbutton = Button(frame, text="Reset", font=("Cooper Black", 15), command=reset_field)
resetbutton.place(x=190, y=180)

if __name__ == "__main__":
    frame.mainloop()

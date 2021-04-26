from tkinter import *
import pyttsx3

root=Tk()
root.title("Text to Speech")
root.geometry("800x500")

def talk():
    engine = pyttsx3.init()
    engine.say(entry.get())
    engine.runAndWait()
    entry.delete(0,END)
entry=Entry(root,font=('arial',30))
entry.pack(pady=20)
button=Button(root,text="Speak",command=talk)
button.pack(pady=20)

root.mainloop()
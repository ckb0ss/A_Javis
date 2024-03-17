from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
from pygame import mixer
root = Tk()
root.geometry("1000x500")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("C:\\Users\\Admin\\Downloads\\ironsnap.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    mixer.init()
    mixer.music.load("C:\\Users\\Admin\\Downloads\\dialogue.mp3")
    mixer.music.play()
    i=0
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()

        time.sleep(0.01)

    root.destroy()
    root.mainloop()


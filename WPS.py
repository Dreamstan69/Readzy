# Wps ke liye algorithm

from tkinter import *
import time

para = "India is one of the youngest superpowers in the world.\n The National bird of India is the peacock, which has\n a very colourful and beautiful tail. The national flower of\n India is Lotus. Lotus comes in many colours, white and pink \nbeing prominent.The National animal of India is the Royal\n Bengal tiger."

words = len(para.split())

# Stop watch code starts:

def start():
    global start_time
    start_time = time.time()

def stop_show():
    global end_time
    end_time = time.time()
    global elapsed_time
    elapsed_time = end_time - start_time
    print(f"Time elapsed: {round(elapsed_time, 2)}")
    wps = words/elapsed_time
    spw = elapsed_time/words
    print(f"Your current WPS (Words per second): {round(wps, 2)}")  
    print(f"Your current SPW (Seconds per word): {round(spw, 2)}")  

# UI code:

root = Tk()

para_label = Label(root, text=para, bg="red",
                   font="comicsansms 23 bold", width=100, height=10)
para_label.pack(fill=X)

Start_btn = Button(root, text="Start", command=start,
                   fg="red", width=25, height=5)
Stop_btn = Button(root, text="Stop", fg="red",
                  width=25, height=5, command=stop_show)

Start_btn.pack(anchor=S, side=TOP)
Stop_btn.pack(side=TOP, anchor=S)

frame = Frame(bg="grey", )

root.title("Readzy")
root.mainloop()

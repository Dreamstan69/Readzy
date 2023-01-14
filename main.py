# playing audio wala algorithm
import os
from playsound import playsound
import threading
import time
from pynput import keyboard

text = open("book.txt",encoding="utf-8").read()     
words_length = len(text.split())
split = text.split()
path = "Audio_tracks"
dir_list = os.listdir(path)
active = True
pause_list = []
status = ""

def linear_search(list, n , key):
    for i in range(0, n):  
        if (list[i] == key):
            return i
    return -1 

def play_sound(args):
    playsound(args)

global i
i = 0
def Pause():
    global active
    active = False
    status = "paused"

def Play():
    global active
    active = True
    status = "playing"
    check_word()

def check_status():
    if status == "paused":
                  Play()
    elif status == "playing":
                  Pause()

def check_word():
    t1 = threading.Thread(target=check_status, args=())
    t1.daemon = True
    t1.start()
    global active
    while active:
        global i
        if status == "paused":
            word = pause_list.pop()
        else:
            word = text.split()[i]

        pause_list.append(word)
        file = word + '.mp3'
        search_result = linear_search(dir_list, len(dir_list), file)
        path = f"Audio_tracks\{file}"
        time.sleep(0.2)
        print(word)
        if search_result == -1:
            print("Audio not found")
        else:
            t2 = threading.Thread(target=play_sound, args=(path,))
            t2.daemon = True
            t2.start()
        i += 1

        if word == "(_stop_)":
            active = False
            break
        
        if status == "paused":
                Play()
        elif status == "playing":
                Pause()
check_word()
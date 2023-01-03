# playing audio wala algorithm
import os
import vlc 

text = open("book.txt",encoding="utf-8").read()
words_length = len(text.split())
split = text.split()
path = "Audio_tracks"
dir_list = os.listdir(path)
global letters
letters = []
audio_tracks = []

def slice_audioname():
    for i in range(0,len(dir_list)):
          term = dir_list[i]
          audio_tracks.append(term)

sliced_audio = slice_audioname() # func udd gaya random variable

def linear_search(list, n , key):
    for i in range(0, n):  
        if (list[i] == key):  
            return i 
    return -1 

print(sliced_audio)
def start():
    for i in range(0,words_length):
        word = split[i]
                
start()

            

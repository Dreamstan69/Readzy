import pygame
import time

pygame.mixer.init()

pygame.mixer.music.load('applause.mp3')
pygame.mixer.music.play()
print("Audio will play for 4 seconds")

time.sleep(10)
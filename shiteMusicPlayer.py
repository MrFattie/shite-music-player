import tkinter as tk
from tkinter import filedialog
import os
import pygame
import random
from sys import exit

root = tk.Tk()
root.withdraw()

pygame.init()
pygame.mixer.init()



file_path = filedialog.askdirectory()
music = []
for i in os.listdir(file_path):
    if '.' in i:
        if '.mp3' in i or '.wav' in i:
            music.append(file_path + '/' + i)
    else:
        for j in os.listdir(file_path + '/' + i):
            if '.mp3' in j or '.wav' in j:
                music.append(file_path + '/' + i + '/' + j)

outOfSongs = False
songPlaying = False
playing = True

nextSong = 0
while True:
    if not songPlaying:
        songPlaying = True
        pygame.mixer.stop()
        randomNum = random.randint(0, len(music) - 1)

        #'nextSong' currently unused
        if nextSong:
            pygame.mixer.Sound(nextSong).play()
            nextSong = 0
        else:
            pygame.mixer.Sound(music[randomNum]).play()

        music.pop(randomNum)
        if not music:
            outOfSongs = True
    if outOfSongs and not songPlaying:
        pygame.quit()
        exit()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and music:
            songPlaying = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if playing:
                pygame.mixer.pause()
                playing = False
            else:
                pygame.mixer.unpause()
                playing = True
    if not pygame.mixer.get_busy():
        songPlaying = False

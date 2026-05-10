import os, json, random
import tkinter
from tkinter import filedialog
import pygame
root = tkinter.Tk()
root.withdraw()

pygame.init()
pygame.mixer.init()

def loadFile():
    music = []
    file_path = filedialog.askopenfilename()
    music.append(file_path)
    return music, file_path
def loadFolder():
    file = open('config.json', 'r')
    config = json.load(file)
    doDirectories = config["doSubDirectories"]
    doShuffle = config["doShuffle"]
    file_path = filedialog.askdirectory()
    music = []
    if file_path:
        for i in os.listdir(file_path):
            if '.' in i:
                if '.mp3' in i or '.wav' in i:
                    music.append(file_path + '/' + i)
            else:
                for j in os.listdir(file_path + '/' + i):
                    if ('.mp3' in j or '.wav' in j) and doDirectories:
                        music.append(file_path + '/' + i + '/' + j)
        file.close()
    if not doShuffle:
        for i in range(len(music)):
            music[i] = music[i].lower()
        music = sorted(music)
    return music, file_path

def nextSong(music, musicLeft):
    file = open('config.json', 'r')
    doShuffle = json.load(file)["doShuffle"]
    pygame.mixer.stop()
    if doShuffle:
        randomNum = random.randint(0, len(music) - 1)
        pygame.mixer.Sound(music[randomNum]).play()
    else:
        randomNum = 0
        pygame.mixer.Sound(musicLeft[randomNum]).play()
    return randomNum
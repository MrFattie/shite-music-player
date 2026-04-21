import pygame, json
import tkinter as tk
from sys import exit
from funcs import *


def displayButton(text, font, textColour, topleft, width, height, colour):
    surf = pygame.Surface((width, height))
    rect = pygame.Rect(topleft[0], topleft[1], width, height)
    surf.fill(colour)
    screen.blit(surf, topleft)
    screen.blit(font.render(text, False, textColour), (topleft[0] + 5, topleft[1]))
    return rect
root = tk.Tk()
root.withdraw()
pygame.init()
screen = pygame.display.set_mode((550, 350), pygame.RESIZABLE)
font = pygame.font.Font('KarmaFuture.ttf', 20)
fontSmall = pygame.font.Font('KarmaFuture.ttf', 15)
yes = pygame.image.load('yes.png').convert_alpha()
yes = pygame.transform.scale_by(yes, 0.125)
no = pygame.image.load('no.png').convert_alpha()
no = pygame.transform.scale_by(no, 0.125)
rect1 = pygame.Rect(0, 0, 0, 0)
rect2 = pygame.Rect(0, 0, 0, 0)
rect3 = pygame.Rect(210, 58, 30, 30)
surf = pygame.Surface((34, 34))
surf.fill('#aababd')
pygame.display.set_caption('Shite Music Player')
colour1 = '#1e2024'
colour2 = '#1e2024'
music = []
musicLeft = []
config = json.load(open('config.json', 'r'))
file_path = ''
num = 0
playing = True
skipSong = False
folderOpened = False
highlight = False
alreadyPlayed = False

while True:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and len(music) > 1:
                skipSong = True
            if event.key == pygame.K_SPACE and music:
                if playing:
                    pygame.mixer.pause()
                    playing = False
                else:
                    pygame.mixer.unpause()
                    playing = True
        if rect1.collidepoint(pygame.mouse.get_pos()):
            colour1 = '#41454d'
            if event.type == pygame.MOUSEBUTTONDOWN:
                music, file_path = loadFolder()
                pygame.mixer.stop()
                musicLeft = music.copy()
                folderOpened = True
                alreadyPlayed = False
        else:
            colour1 = '#1e2024'
        if rect2.collidepoint(pygame.mouse.get_pos()):
            colour2 = '#41454d'
            if event.type == pygame.MOUSEBUTTONDOWN:
                music, file_path = loadFile()
                pygame.mixer.stop()
                musicLeft = music.copy()
                folderOpened = False
                alreadyPlayed = False
        else:
            colour2 = '#1e2024'
        if rect3.collidepoint(pygame.mouse.get_pos()):
            highlight = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not config["doSubDirectories"]:
                    config["doSubDirectories"] = True
                    with open('config.json', 'w') as file:
                        json.dump(config, file)
                else:
                    config["doSubDirectories"] = False
                    with open('config.json', 'w') as file:
                        json.dump(config, file)
        else:
            highlight = False



    #display
    screen.fill('#929ba8')
    rect1 = displayButton('Open Folder...', font, 'white', [50, 60], 150, 30, colour1)
    rect2 = displayButton('Open File...', font, 'white', [50, 20], 120, 30, colour2)
    if config["doSubDirectories"] == True:
        screen.blit(yes, (210, 58))
        screen.blit(font.render('Include sub-folders', False, 'green'), (255, 62))
    else:
        screen.blit(no, (210, 58))
        screen.blit(font.render('Include sub-folders', False, 'firebrick'), (255, 62))
    if highlight:
        if config["doSubDirectories"] == True:
            yes.blit(surf, (0, 0), special_flags=pygame.BLEND_MAX)
        else:
            no.blit(surf, (0, 0), special_flags=pygame.BLEND_MAX)
    else:
        surf = pygame.Surface((34, 34))
        surf.fill('#aababd')
        yes = pygame.image.load('yes.png').convert_alpha()
        yes = pygame.transform.scale_by(yes, 0.125)
        no = pygame.image.load('no.png').convert_alpha()
        no = pygame.transform.scale_by(no, 0.125)



    #music

    if len(musicLeft) > 1:
        screen.blit(fontSmall.render('Folder opened is \'' + file_path + '\'', False, 'black'), (80, 120))
        screen.blit(fontSmall.render('Song currently playing is \'' + music[num].replace(file_path, '') + '\'', False, 'black'), (80, 150))
        if not pygame.mixer.get_busy() or skipSong:
            skipSong = False
            num = nextSong(music)
            while music[num] not in musicLeft:
                num = nextSong(music)
                
            newNum = musicLeft.index(music[num])
            musicLeft.pop(newNum)
    elif len(musicLeft) == 1:
        if folderOpened:
            screen.blit(fontSmall.render('Folder opened is \'' + file_path + '\'', False, 'black'), (80, 120))
            screen.blit(fontSmall.render('Song currently playing is \'' + musicLeft[0].replace(file_path, '') + '\'', False, 'black'), (80, 150))
        else:
            screen.blit(fontSmall.render('You have not opened a folder.', False, 'black'), (80, 120))
            screen.blit(fontSmall.render('Song currently playing is:\n\'' + musicLeft[0] + '\'', False, 'black'), (50, 150))
        if not pygame.mixer.get_busy() and not alreadyPlayed:
            pygame.mixer.Sound(musicLeft[0]).play()
            alreadyPlayed = True
        

    pygame.display.update()
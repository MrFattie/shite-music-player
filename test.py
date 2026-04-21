import pygame
from sys import exit

def displayButton(text, font, textColour, topleft, width, height, colour):
    surf = pygame.Surface((width, height))
    rect = pygame.Rect(topleft[0], topleft[1], width, height)
    surf.fill(colour)
    screen.blit(surf, topleft)
    screen.blit(font.render(text, False, textColour), (topleft[0] + 5, topleft[1]))
    return rect

pygame.init()
screen = pygame.display.set_mode((550, 350))
font = pygame.font.Font('KarmaFuture.ttf')
rect1 = pygame.Rect(0, 0, 0, 0)
rect2 = pygame.Rect(0, 0, 0, 0)
pygame.display.set_caption('Shite Music Player')
colour1 = '#1e2024'
colour2 = '#1e2024'

while True:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if rect1.collidepoint(pygame.mouse.get_pos()):
            colour1 = '#41454d'
            if event.type == pygame.MOUSEBUTTONDOWN:
                
        else:
            colour1 = '#1e2024'
        if rect2.collidepoint(pygame.mouse.get_pos()):
            colour2 = '#41454d'
        else:
            colour2 = '#1e2024'

    #display
    screen.fill('#929ba8')
    rect1 = displayButton('Open Folder...', font, 'white', [50, 60], 150, 30, colour1)
    rect2 = displayButton('Open File...', font, 'white', [50, 20], 120, 30, colour2)
    pygame.display.update()
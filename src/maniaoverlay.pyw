import pygame
import sys
from time import sleep as wait
import keyboard

#function for getting a tuple from a string. used for reading and easily storing config.txt's rgb values.
def string_to_tuple(input):
    string = input.replace("(","")
    string = string.replace(")","")
    string = tuple(map(int, string.split(',')))

    return string

#reads the config document and separates it by lines, then stores the necessary lines.
with open('..\\config.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    keys = [lines[5],lines[8],lines[11],lines[14]]
    colorOn = string_to_tuple(lines[17])
    colorOff = string_to_tuple(lines[20])
    colorBG = string_to_tuple(lines[23])

key1 = False
key2 = False
key3 = False
key4 = False

waiting1 = False
waiting2 = False
waiting3 = False
waiting4 = False

i=0

keyspressed = 0
nps = 0

pygame.init()

font = pygame.font.SysFont('Arial', 20)
fontBig = pygame.font.SysFont('Arial',22)

windowsize = (280,60)
screen = pygame.display.set_mode(windowsize)
pygame.display.set_caption('Universal Mania Overlay')

gameloop = True #variable for the quit system. only used in early dev-stages; sys.exit() is now used in later releases.

clock = pygame.time.Clock()

key1gui = pygame.Surface((50,50))
key1gui.fill(colorOff)

key2gui = pygame.Surface((50,50))
key2gui.fill(colorOff)

key3gui = pygame.Surface((50,50))
key3gui.fill(colorOff)

key4gui = pygame.Surface((50,50))
key4gui.fill(colorOff)

info = pygame.Surface((50,50))
info.fill((127,127,127))

key1txt = font.render(keys[0].upper(),True,(255,255,255))
key2txt = font.render(keys[1].upper(),True,(255,255,255))
key3txt = font.render(keys[2].upper(),True,(255,255,255))
key4txt = font.render(keys[3].upper(),True,(255,255,255))
info1txt = fontBig.render('NPS',True,(255,255,255))

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0,255,0))

    i+=1

    if i==61:
        i = 0
        nps = keyspressed
        keyspressed = 0

    info2txt = font.render(str(nps),True,(255,255,255))

    #gets assigned keys pressed
    if keyboard.is_pressed(keys[0]):
        key1 = True
        key1gui.fill(colorOn)
        if not waiting1:
            keyspressed += 1
        waiting1 = True
    else:
        key1 = False
        key1gui.fill(colorOff)
        waiting1 = False

    if keyboard.is_pressed(keys[1]):
        key2 = True
        key2gui.fill(colorOn)
        if not waiting2:
            keyspressed += 1
        waiting2 = True
    else:
        key2 = False
        key2gui.fill(colorOff)
        waiting2 = False

    if keyboard.is_pressed(keys[2]):
        key3 = True
        key3gui.fill(colorOn)
        if not waiting3:
            keyspressed += 1
        waiting3 = True
    else:
        key3 = False
        key3gui.fill(colorOff)
        waiting3 = False

    if keyboard.is_pressed(keys[3]):
        key4 = True
        key4gui.fill(colorOn)
        if not waiting4:
            keyspressed += 1
        waiting4 = True
    else:
        key4 = False
        key4gui.fill(colorOff)
        waiting4 = False

    #------------------------------------------- main area where all surfaces undergo block transfer
    screen.blit(key1gui,((5,5)))
    screen.blit(key2gui,((60,5)))
    screen.blit(key3gui,((115,5)))
    screen.blit(key4gui,((170,5)))
    screen.blit(key1txt,((24,18)))
    screen.blit(key2txt,((80,18)))
    #test to see if key3 is ; and/or key 4 is ', because i use keys a s ; ' which makes it off center a little. kinda stupid
    if keys[2] == ";":
        screen.blit(key3txt,((138,18)))
    else:
        screen.blit(key3txt,((135,18)))
    if keys[3] == "\'":
        screen.blit(key4txt,((194,18)))
    else:
        screen.blit(key4txt,((192,18)))
    screen.blit(info,((225,5)))
    screen.blit(info1txt,((232,7)))
    screen.blit(info2txt,((232,29)))

    pygame.display.update()
    clock.tick(60) #restricts game to 60fps
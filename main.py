import time
import os
import pygame
from time import sleep
import sys

#set constant variables
SCREEN_WIDTH = 144
SCREEN_HEIGHT = 256
SCALE = 3

#set variables
i = 0

#open the file we want to read
with open("meinkampf.txt", "r") as meinKampf:
    textDoc = meinKampf.read()

def main():

    #set variables and get global variables
    global i
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    global SCALE

    #initialize pygame and set display for the window
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption("Speed Reader")
    screen = pygame.display.set_mode((SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE))

    #initialize font
    pygame.font.init()
    speedFont = pygame.font.SysFont('Comic Sans MS', 30)
    word = ""

    try:
        #loop to create each word
        while textDoc[i] != " ":
            word = word + textDoc[i]
            i = i + 1
            if textDoc[i] == "\n":
                i = i + 1

    except:
        #don't error out at the end of the file
        word = "END OF FILE"

    #create a textsurface
    textsurface = speedFont.render(word, 1, (255, 255, 255))

    #display the text
    screen.blit(textsurface,(0, SCREEN_HEIGHT * SCALE / 2))
    pygame.display.flip()

    #display the word in a readable manner in the console window
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print word

    #wait before going again
    sleep(0.12)
    i = i + 1

    #repeat until the end of the file
    if word != "END OF FILE":
        main()

#call main method
main()

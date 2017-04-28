import time
import os
import pygame
from time import sleep
import sys
from pygame.locals import *
# import docx

#set constant variables
SCREEN_WIDTH = 144
SCREEN_HEIGHT = 256
SCALE = 3

color = (255, 255, 255)

#set variables
i = 0

#open the file we want to read
with open("meinkampf.txt", "r") as meinKampf:
    textDoc = meinKampf.read()
    textDoc += " @FIN@"

# doc = docx.Document('Essay 3.docx')

def main():
    running = True

    while running:
        #set variables and get global variables
        global i
        global SCREEN_WIDTH
        global SCREEN_HEIGHT
        global SCALE
        global color

        debug = True

        corner1 = (28,18)  #Top Left corner of button 1
        corner2 = (56,18)  #Top Left corner of button 2

        image_length = 100 #length of the buttons
        image_height = 100 #height of the buttons

        #initialize pygame and set display for the window
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption("Speed Reader")
        screen = pygame.display.set_mode((SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE))

        pygame.draw.line(screen, (255, 255, 255), (0, SCREEN_HEIGHT * SCALE / 5 - 30), (SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE / 5 - 30), 1)
        pygame.draw.line(screen, (255, 255, 255), (0, SCREEN_HEIGHT * SCALE / 5 + 30 + 40), (SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE / 5 + 30 + 40), 1)
        pygame.draw.line(screen, (255, 255, 255), (SCREEN_WIDTH * SCALE / 2, SCREEN_HEIGHT * SCALE / 5 - 30), (SCREEN_WIDTH * SCALE / 2, SCREEN_HEIGHT * SCALE / 5 - 20), 1)
        pygame.draw.line(screen, (255, 255, 255), (SCREEN_WIDTH * SCALE / 2, SCREEN_HEIGHT * SCALE / 5 + 30 + 40), (SCREEN_WIDTH * SCALE / 2, SCREEN_HEIGHT * SCALE / 5 + 20 + 40), 1)

        #initialize font
        pygame.font.init()
        speedFont = pygame.font.SysFont('Helvetica', 30)
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
            word = "FIN"

            #create a textsurface
            textsurface = speedFont.render(word, 1, (color))

            #calculate the center of the word
            x = ((SCREEN_WIDTH / 2) * SCALE - (textsurface.get_rect().width / 2))

            #display the text
            screen.blit(textsurface, (x, SCREEN_HEIGHT * SCALE / 5))
            pygame.display.flip()
            sleep(5)

        #repeat until the end of the file
        if word != "FIN":

            #create a textsurface
            textsurface = speedFont.render(word, 1, (color))

            #calculate the center of the word
            x = ((SCREEN_WIDTH / 2) * SCALE - (textsurface.get_rect().width / 2))

            #display the text
            screen.blit(textsurface, (x, SCREEN_HEIGHT * SCALE / 5))
            pygame.display.flip()

            #display the word in a readable manner in the console window
            if debug:
                print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                print word

            #wait before going again
            sleep(0.12)
            i = i + 1

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if (mouse_x >= corner1[0]) and (mouse_x <= corner1[0]+image_length) and (mouse_y >= corner1[1]) and (mouse_y <= corner1[1]+image_height):
                        print ("Button one is selected")
                        button1=True
                        button2=False
                    elif (mouse_x >= corner2[0]) and (mouse_x <= corner2[0]+image_length) and (mouse_y >= corner2[1]) and (mouse_y <= corner2[1]+image_height):
                        print ("Button two is selected")
                        button1=False
                        button2=True
                    else:
                        print ("That's not a button")
                        color = (255, 0, 0)
                        button1=False
                        button2=False

            #loop through program
            main()

#call main method
main()

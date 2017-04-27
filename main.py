import time
import os
import pygame
from time import sleep
import sys
# import docx

#set constant variables
SCREEN_WIDTH = 144
SCREEN_HEIGHT = 256
SCALE = 3

#set variables
i = 0

#open the file we want to read
with open("meinkampf.txt", "r") as meinKampf:
    textDoc = meinKampf.read()

# doc = docx.Document('Essay 3.docx')

def main():

    # print doc.paragraphs[9].text

    #set variables and get global variables
    global i
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    global SCALE

    debug = True

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
        # word = "FIN"
        hi = "hi"

    #create a textsurface
    textsurface = speedFont.render(word, 1, (255, 255, 255))

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

    #repeat until the end of the file
    if word != "FIN":
        main()

#call main method
main()

import time
import os
import pygame
from time import sleep
import sys
from pygame.locals import *
import tkFileDialog as filedialog
from Tkinter import *
import Tkinter as ttk
from ttk import *

#set constant variables
SCREEN_WIDTH = 144
SCREEN_HEIGHT = 256
SCALE = 2

color = (255, 255, 255)

#set variables
i = 0

def speedreader(textDoc):

    running = True
    clock = pygame.time.Clock()
    speed = 0.2
    white = (255, 255, 255)
    black = (0, 0, 0)

    while True:
        clock.tick(60)
        if running:

            #set variables and get global variables
            global i
            global SCREEN_WIDTH
            global SCREEN_HEIGHT
            global SCALE
            global color

            debug = False

            corner1 = (25, SCREEN_HEIGHT * SCALE - 75)  #Top Left corner of button 1
            corner2 = (SCREEN_WIDTH * SCALE - 125, SCREEN_HEIGHT * SCALE - 75)  #Top Left corner of button 2

            corner3 = (25, SCREEN_HEIGHT * SCALE - 150)  #Top Left corner of button 1
            corner4 = (SCREEN_WIDTH * SCALE - 125, SCREEN_HEIGHT * SCALE - 150)  #Top Left corner of button 2

            image_length = 100 #length of the buttons
            image_height = 50 #height of the buttons

            #initialize pygame and set display for the window
            pygame.init()
            os.environ['SDL_VIDEO_CENTERED'] = '1'
            pygame.display.set_caption("Speed Reader")
            screen = pygame.display.set_mode((SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE))

            if color == white:
                screen.fill(black)

            if color == black:
                screen.fill(white)

            #draw lines on the screen
            pygame.draw.line(screen, (color), (0, SCREEN_HEIGHT * SCALE / 5 - 30), (SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE / 5 - 30), 1)
            pygame.draw.line(screen, (color), (0, SCREEN_HEIGHT * SCALE / 5 + 30 + 40), (SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE / 5 + 30 + 40), 1)
            pygame.draw.line(screen, (color), (SCREEN_WIDTH * SCALE / 2, SCREEN_HEIGHT * SCALE / 5 - 30), (SCREEN_WIDTH * SCALE / 2, SCREEN_HEIGHT * SCALE / 5 - 20), 1)
            pygame.draw.line(screen, (color), (SCREEN_WIDTH * SCALE / 2, SCREEN_HEIGHT * SCALE / 5 + 30 + 40), (SCREEN_WIDTH * SCALE / 2, SCREEN_HEIGHT * SCALE / 5 + 20 + 40), 1)

            #draw the buttons
            pygame.draw.rect(screen, (0, 0, 0), (25, SCREEN_HEIGHT * SCALE - 75, 100, 50), 0)
            pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH * SCALE - 125, SCREEN_HEIGHT * SCALE - 75, 100, 50), 0)

            pygame.draw.rect(screen, (255, 0, 0), (25, SCREEN_HEIGHT * SCALE - 150, 100, 50), 0)
            pygame.draw.rect(screen, (0, 255, 0), (SCREEN_WIDTH * SCALE - 125, SCREEN_HEIGHT * SCALE - 150, 100, 50), 0)

            #initialize font
            pygame.font.init()
            speedFont = pygame.font.SysFont('Helvetica', 30)
            otherSpeedFont = pygame.font.SysFont('Helvetica', 18)
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

            #repeat until the end of the file
            if word != "FIN":

                wpm = 60 / speed

                #create a textsurface
                textsurface = speedFont.render(word, 1, (color))
                wpmsurface = otherSpeedFont.render(str(round(wpm, -1)) + " words per minute", 1, (color))

                #calculate the center of the word
                x = ((SCREEN_WIDTH / 2) * SCALE - (textsurface.get_rect().width / 2))
                newx = ((SCREEN_WIDTH / 2) * SCALE - (wpmsurface.get_rect().width / 2))

                #display the text
                screen.blit(textsurface, (x, SCREEN_HEIGHT * SCALE / 5))
                screen.blit(wpmsurface, (newx, SCREEN_HEIGHT * SCALE - 200))

                pygame.display.flip()

                #display the word in a readable manner in the console window
                if debug:
                    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    print word

                #wait before going again

                sleep(speed)
                i = i + 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit();
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        if (mouse_x >= corner1[0]) and (mouse_x <= corner1[0]+image_length) and (mouse_y >= corner1[1]) and (mouse_y <= corner1[1]+image_height):
                            color = white

                        elif (mouse_x >= corner2[0]) and (mouse_x <= corner2[0]+image_length) and (mouse_y >= corner2[1]) and (mouse_y <= corner2[1]+image_height):
                            color = black

                        elif (mouse_x >= corner3[0]) and (mouse_x <= corner3[0]+image_length) and (mouse_y >= corner3[1]) and (mouse_y <= corner3[1]+image_height):
                            speed = speed + 0.02
                            if debug:
                                print "Speed", speed

                        elif (mouse_x >= corner4[0]) and (mouse_x <= corner4[0]+image_length) and (mouse_y >= corner4[1]) and (mouse_y <= corner4[1]+image_height):
                            speed = speed - 0.02
                            if debug:
                                print "Speed", speed

                        else:
                            color = (255, 255, 255)
                            if debug:
                                print ("That's not a button")
                            button1=False
                            button2=False

def pasteorsearch(pors):
    #print(pors)
    if pors == 'Search':
        os.system('cls')

        #create open filedialog
        root = ttk.Tk()
        root.withdraw()
        path = filedialog.askopenfilename()

        #open the file we want to read
        with open(path, "r") as textFile:
            textDoc = textFile.read()
            textDoc += " @FIN@"
        speedreader(textDoc)

    elif pors == 'Paste':
        root = ttk.Tk()

        mainframe = Frame(root)
        # mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S ))
        # mainframe.columnconfigure(0, weight = 1)
        # mainframe.rowconfigure(0, weight = 1)
        # mainframe.pack(pady = 25, padx = 50)

        textBox = Text(root, height = 25, width = 40)
        sBar = Scrollbar(root)
        sBar.config(command = textBox.yview)
        textBox.config(yscrollcommand = sBar.set)
        textBox.grid(row = 1, column = 1)

        button = ttk.Button(root, text = "Select", command = lambda: speedreader(textBox.get(0.0, END)))
        button.grid(row = 2, column = 1)

        textBox.focus_force()
        mainloop()

        # uAns = sys.stdin.readlines()
        # uAns = " ".join(uAns)
        # uAns += " @FIN@"
        # print (uAns)
        # main(uAns)

#paste or get from document
def main():
    root = Tk()
    root.title("Speed Reader")

    # Add a grid
    mainframe = Frame(root)
    mainframe.grid(column = 0,row = 0, sticky = (N, W, E, S ))
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 25, padx = 50)

    # Create a Tkinter variable
    tkvar = StringVar(root)

    # Dictionary with options
    choices = {'Paste', 'Search', 'Choose Value'}
    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    Label(mainframe, text="Would you like to paste or search the device for your desired text?").grid(row = 1, column = 1)
    popupMenu.grid(row = 2, column = 1)
    tkvar.set('Choose Value') # set the default option
    button = ttk.Button(mainframe, text ="Select", command = lambda: pasteorsearch(tkvar.get()))
    button.grid(row = 3, column = 1)

    # on change dropdown value
    # def change_dropdown(*args):
        # print(tkvar.get())

    # link function to change dropdown
    # tkvar.trace('w', change_dropdown)

    root.mainloop()

main()

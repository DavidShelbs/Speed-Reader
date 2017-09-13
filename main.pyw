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
# SCREEN.current_w
# SCREEN.current_h
SCALE = 1

color = (255, 255, 255)

#set variables
i = 0

def speedreader():

    running = True
    clock = pygame.time.Clock()
    speed = 0.2
    white = (255, 255, 255)
    black = (0, 0, 0)
    rbLogo = pygame.image.load('rollickboonlogo.jpg')
    textDoc = 'sample_text.txt'

    while True:
        clock.tick(60)
        if running:

            #set variables and get global variables
            global i
            # global SCREEN
            # global SCREEN
            global SCALE
            global color

            debug = False

            #initialize pygame and set display for the window
            pygame.init()
            SCREEN = pygame.display.Info()
            os.environ['SDL_VIDEO_CENTERED'] = '1'
            pygame.display.set_caption("Rollick Reader")
            pygame.display.set_icon(rbLogo)
            screen = pygame.display.set_mode((800, 600))

            image_length = SCREEN.current_w * .75 / 4 #length of the buttons
            image_height = 25 #height of the buttons

            grey = (50, 50, 50)
            darkGrey = (25, 25, 25)
            vDarkGrey = (15, 15, 15)

            screen.fill(white)

            if color == white:
                screen.fill(black)

            if color == black:
                screen.fill(white)

            corner1 = (SCREEN.current_w * .75 - SCREEN.current_w * .75, SCREEN.current_h * SCALE / 2)  #Top Left corner of button 1
            corner2 = (SCREEN.current_w * .75 - SCREEN.current_w * .75 * .75, SCREEN.current_h * SCALE / 2)  #Top Left corner of button 2

            corner3 = (25, SCREEN.current_h * SCALE - 150)  #Top Left corner of button 1
            corner4 = (SCREEN.current_w * SCALE * .75 - 125, SCREEN.current_h * SCALE - 150)  #Top Left corner of button 2

            #draw lines on the screen
            pygame.draw.line(screen, (vDarkGrey), (0, SCREEN.current_h * SCALE / 4 - 70), (SCREEN.current_w * SCALE * .75, SCREEN.current_h * SCALE / 4 - 70),   3)
            pygame.draw.line(screen, (vDarkGrey), (0, SCREEN.current_h * SCALE / 4 + 70), (SCREEN.current_w * SCALE * .75, SCREEN.current_h * SCALE / 4 + 70), 3)

            pygame.draw.line(screen, (vDarkGrey), (SCREEN.current_w * SCALE * (.75 / 2), SCREEN.current_h * SCALE / 4 - 70), (SCREEN.current_w * SCALE * (.75 / 2), SCREEN.current_h * SCALE / 4 - 50), 3)
            pygame.draw.line(screen, (vDarkGrey), (SCREEN.current_w * SCALE * (.75 / 2), SCREEN.current_h * SCALE / 4 + 70), (SCREEN.current_w * SCALE * (.75 / 2), SCREEN.current_h * SCALE / 4 + 50), 3)

            pygame.draw.rect(screen, (grey), (0, SCREEN.current_h * SCALE / 2, SCREEN.current_w * .75 - 1, SCREEN.current_h / 2), 0)

            #draw the buttons
            pygame.draw.rect(screen, (255, 255, 255), (SCREEN.current_w * .75 - SCREEN.current_w * .75, SCREEN.current_h * SCALE / 2, image_length, image_height), 0)
            pygame.draw.rect(screen, (255, 255, 255), (SCREEN.current_w * .75 - SCREEN.current_w * .75 * .75, SCREEN.current_h * SCALE / 2, image_length, image_height), 0)

            pygame.draw.rect(screen, (255, 255, 255), (SCREEN.current_w * .75 - SCREEN.current_w * .75 / 2, SCREEN.current_h * SCALE / 2, image_length, image_height), 0)
            pygame.draw.rect(screen, (255, 255, 255), (SCREEN.current_w * .75 - SCREEN.current_w * .75 * .25, SCREEN.current_h * SCALE / 2, image_length, image_height), 0)

            pygame.draw.line(screen, (vDarkGrey), (SCREEN.current_w * SCALE * .75, 0), (SCREEN.current_w * SCALE * .75, SCREEN.current_h), 3)
            pygame.draw.line(screen, (vDarkGrey), (1, 0), (1, SCREEN.current_h), 3)
            pygame.draw.line(screen, (vDarkGrey), (0, SCREEN.current_h - 2), (SCREEN.current_w, SCREEN.current_h - 2), 3)

            pygame.draw.line(screen, (vDarkGrey), (0, SCREEN.current_h * SCALE / 2 - 2), (SCREEN.current_w * SCALE * .75, SCREEN.current_h * SCALE / 2 - 2), 3)

            pygame.display.flip()

            # initialize font
            pygame.font.init()
            speedFont = pygame.font.SysFont('Helvetica', 30)
            otherSpeedFont = pygame.font.SysFont('Helvetica', 18)
            word = ""

            # while i < 6:
            #     i = 5
            #     startsurface = speedFont.render(i, 1, (color))
            #     newxx = ((SCREEN.current_w / 2) * SCALE - (startsurface.get_rect().width / 2))
            #     screen.blit(startsurface, (newxx, SCREEN.current_h * SCALE / 5))
            #     pygame.display.flip()
            #     i = i - 1

            i = 0

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
                x = ((SCREEN.current_w * .75/ 2) * SCALE - (textsurface.get_rect().width / 2))

                #display the text
                screen.blit(textsurface, (x, SCREEN.current_h * SCALE / 5))
                pygame.display.flip()

            #repeat until the end of the file
            if word != "FIN":

                wpm = 60 / speed

                #create a textsurface
                textsurface = speedFont.render(word, 1, (color))
                wpmsurface = otherSpeedFont.render(str(round(wpm, -1)) + " words per minute", 1, (color))

                #calculate the center of the word
                x = ((SCREEN.current_w * .75/ 2) * SCALE - (textsurface.get_rect().width / 2))
                newx = ((SCREEN.current_w * .75/ 2) * SCALE - (textsurface.get_rect().width / 2))

                #display the text
                screen.blit(textsurface, (x, SCREEN.current_h * SCALE / 5))
                screen.blit(wpmsurface, (newx, SCREEN.current_h * SCALE - 200))

                pygame.display.flip()

                #display the word in a readable manner in the console window
                if debug:
                    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print (word)

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
                            color = black

                        elif (mouse_x >= corner2[0]) and (mouse_x <= corner2[0]+image_length) and (mouse_y >= corner2[1]) and (mouse_y <= corner2[1]+image_height):
                            color = white

                        elif (mouse_x >= corner3[0]) and (mouse_x <= corner3[0]+image_length) and (mouse_y >= corner3[1]) and (mouse_y <= corner3[1]+image_height):
                            speed = speed + 0.02
                            if debug:
                                print ("Speed", speed)

                        elif (mouse_x >= corner4[0]) and (mouse_x <= corner4[0]+image_length) and (mouse_y >= corner4[1]) and (mouse_y <= corner4[1]+image_height):
                            speed = speed - 0.02
                            if debug:
                                print ("Speed", speed)

                        else:
                            if debug:
                                print ("That's not a button")
                            button1=False
                            button2=False

speedreader()

def pasteorsearch(pors):
    #print(pors)
    if pors == 'Search':
        os.system('cls')

        #create open filedialog
        root = ttk.Tk()
        root.withdraw()
        path = filedialog.askopenfilename(initialdir = "C:/")

        #open the file we want to read
        with open(path, "r") as textFile:
            textDoc = textFile.read()

        speedreader(textDoc)

    elif pors == 'Paste':
        root = ttk.Tk()
        root.title("Rollick Reader")
        # mainframe = Frame(root)
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

def main():
    pygame.init()
    SCREEN = pygame.display.Info()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption("Rollick Reader")
    pygame.display.set_icon(pygame.image.load('rollickboonlogo.jpg'))
    # screen = pygame.display.set_mode((SCREEN.current_w * SCALE, SCREEN.current_h * SCALE))
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.font.init()
    startFont = pygame.font.SysFont('Audiowide.ttf', 85)

    #create a textsurface
    starttextsurface = startFont.render("Welcome", 1, (color))
    starttextsurface1 = startFont.render("to", 1, (color))
    starttextsurface2 = startFont.render("Rollick", 1, (color))
    starttextsurface3 = startFont.render("Reader", 1, (color))

    #calculate the center of the word
    x = ((SCREEN.current_w / 2) * SCALE - (starttextsurface.get_rect().width / 2))
    x1 = ((SCREEN.current_w / 2) * SCALE - (starttextsurface1.get_rect().width / 2))
    x2 = ((SCREEN.current_w / 2) * SCALE - (starttextsurface2.get_rect().width / 2))
    x3 = ((SCREEN.current_w / 2) * SCALE - (starttextsurface3.get_rect().width / 2))

    #display the text
    screen.blit(starttextsurface, (x, SCREEN.current_h * SCALE / 5))
    screen.blit(starttextsurface1, (x1, SCREEN.current_h * SCALE / 5 + 60))
    screen.blit(starttextsurface2, (x2, SCREEN.current_h * SCALE / 5 + 120))
    screen.blit(starttextsurface3, (x3, SCREEN.current_h * SCALE / 5 + 180))

    sleep(1)

    pygame.display.flip()

    sleep(3)

    starttextsurface = startFont.render("Created by:", 1, (color))
    starttextsurface1 = startFont.render("David Shelby", 1, (color))

    x = ((SCREEN.current_w / 2) * SCALE - (starttextsurface.get_rect().width / 2))
    x1 = ((SCREEN.current_w / 2) * SCALE - (starttextsurface1.get_rect().width / 2))

    screen.blit(starttextsurface, (x, SCREEN.current_h * SCALE / 5 + 280))
    screen.blit(starttextsurface1, (x1, SCREEN.current_h * SCALE / 5 + 340))

    pygame.display.flip()

    sleep(2)

    screen.fill((0, 0, 0))
    pygame.display.update()

    pygame.display.quit()

    # root = Tk()
    # root.iconbitmap(default = 'rollickboonlogo.ico')
    # root.title("Rollick Reader")
    #
    # # Add a grid
    # mainframe = Frame(root)
    # mainframe.grid(column = 0,row = 0, sticky = (N, W, E, S ))
    # mainframe.columnconfigure(0, weight = 1)
    # mainframe.rowconfigure(0, weight = 1)
    # mainframe.pack(pady = 25, padx = 50)
    #
    # # Create a Tkinter variable
    # tkvar = StringVar(root)
    #
    # # Dictionary with options
    # choices = {'Paste', 'Search', 'Choose Value'}
    # popupMenu = OptionMenu(mainframe, tkvar, *choices)
    # Label(mainframe, text="Would you like to paste or search the device for your desired text?").grid(row = 1, column = 1)
    # popupMenu.grid(row = 2, column = 1)
    # tkvar.set('Choose Value') # set the default option
    # button = ttk.Button(mainframe, text ="Select", command = lambda: pasteorsearch(tkvar.get()))
    # button.grid(row = 3, column = 1)
    #
    # # on change dropdown value
    # # def change_dropdown(*args):
    #     # print(tkvar.get())
    #
    # # link function to change dropdown
    # # tkvar.trace('w', change_dropdown)
    #
    # root.mainloop()
    speedreader()

main()

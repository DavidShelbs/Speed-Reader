import time
import os
import pygame
from time import sleep

i = 0
SPEED = 400
wordsPerSecond = 60 / SPEED
with open("meinkampf.txt", "r") as meinKampf:
    textDoc = meinKampf.read()

def main():
    word = ""
    global i
    global SPEED
    global wordsPerSecond

    try:
        while textDoc[i] != " ":
            word = word + textDoc[i]
            i = i + 1
            if textDoc[i] == "\n":
                i = i + 1

    except:
        word = "END OF FILE"

    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"    
    print word
    sleep(0.12)
    i = i + 1

    if word != "END OF FILE":
        main()

main()

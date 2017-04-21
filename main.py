import time
import os
import pygame

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

    while textDoc[i] != " ":
        word = word + textDoc[i]
        i = i + 1

    time.sleep(1)
    print word
    i = i + 1
    main()

main()

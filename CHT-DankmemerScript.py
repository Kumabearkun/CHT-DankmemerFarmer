#Welcome to HitRecord's Dankmemer Script
#Credits to Swayx113 for the template, you can find him in GitHub!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#DO NOT TOUCH IF YOU DON"T KNOW HOW TO MODIFY THIS
import pynput
import random
import time
from pynput.keyboard import Key, Controller

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#These are the choices groups for (random.choice(Choice group)) you can freely edit them if the changed

#For pls pm
postmeme = ["f", "r", "i", "c", "k"] 

#For pls trivia
trivia = ["a", "b", "c", "d"] 

#For Pls hl
hl = ["high", "low"]

#You can freely edit them but you must have 3-4 words in there to avoid being detected by dankmemer
words = ["I like bread", "bread", "Perhaps", "bruh", "I love this bot"]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
keyboard = Controller()
i = 0

while i < 1:

    keyboard.type('pls hunt')
    keyboard.press(Key.enter)
    time.sleep(2)
    
    keyboard.type(random.choice(words))
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type(random.choice(words))
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type('pls meme')
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type('pls hl')
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type(random.choice(potato))
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type(random.choice(words))
    keyboard.press(Key.enter)
    time.sleep(2)
    
    keyboard.type('pls trivia')
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type(random.choice(quiz))
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type(random.choice(words))
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type('pls fish')
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type('pls pm')
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type(random.choice(postmeme))
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type('pls meme')
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type('pls beg')
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type(random.choice(words))
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type('pls slots 100')
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type('pls snakeeyes 100')
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type('pls bal')
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type(random.choice(words))
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type('pls dep all')
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type(random.choice(words))
    keyboard.press(Key.enter)
    time.sleep(2)

    keyboard.type(random.choice(words))
    keyboard.press(Key.enter)
    time.sleep(2)

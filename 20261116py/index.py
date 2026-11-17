from machine import Pin
import time

flash = Pin(4, Pin.OUT)
flash.value(0)

print("BOOT OK")        

morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..'
}


def morseeng(mor):
    global morse
    answer = []
    for i in mor:
        if i in morse:
            answer += morse[i]
            answer += " "
    for o in answer:
        if o == '.':
            flash.value(1)
            time.sleep(0.2)
            flash.value(0)
            time.sleep(0.2)
        elif o == '-':
            flash.value(1)
            time.sleep(0.6)
            flash.value(0)
            time.sleep(0.2)
        else :
            time.sleep(0.4)
            

morseeng('sos')
        
    

    
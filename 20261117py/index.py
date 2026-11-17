from machine import Pin
import time
import morse

flash = Pin(4, Pin.OUT)
flash.value(0)

print("BOOT OK")        

def mossig(inputmos):
    answer = []
    for i in inputmos:
        obj = getattr(morse, f"morse{i}", None)
        if obj != None:
            answer.append(obj.moscall[i])        
        elif i == ' ':
            answer.append(' ')
    
    print(answer)
    
    for i in answer:
        for o in i:
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
            elif o == ' ':
                time. sleep(1.0)
        time.sleep(0.4)

mossig('sos')

    
    
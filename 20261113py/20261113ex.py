import re

morse = { '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z'}

def solution(letter):
    ansewr = ''
    while len(letter) > 0:
        i = letter.partition(' ')[0]
        if i in morse:
            ansewr += morse[i]
            letter.lstrip(i)
            letter.lstrip(' ')
            
    return ''.join(ansewr)

print(solution('.... . .-.. .-.. ---'))
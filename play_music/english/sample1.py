import threading
import subprocess as sb
import random
import os
import speech_recognition as sr
#import keyboard as kb

def fun(args):    
    sb.Popen(['celluloid',args])

t=threading.Thread(target=fun,args=('a.mp3',))
t.start()
r=sr.Recognizer()
print('Say play music')
with sr.Microphone() as source:
    audio = r.listen(source,timeout=5,phrase_time_limit=5)  
a=r.recognize_google(audio)
if 'play' and 'music' in a:
    app=sb.getoutput(xdg-mime query default `xdg-mime query filetype "$(find ~ / -iname *.wav -print -quit)"`)
    while True:
        try:
            print('Say')
            with sr.Microphone() as source:
                audio = r.listen(source,timeout=5,phrase_time_limit=5)
            a=r.recognize_google(audio)
            print(a)
        except:
            print()
        try:
            if 'quit' in a or 'stop' in a or 'exit' in a:
                sb.getoutput('pkill celluloid')
                break
            elif 'change' in a:
                sb.getoutput('pkill celluloid')
                t=threading.Thread(target=fun,args=('b.mp3',))
                t.start()
        except:
            print()






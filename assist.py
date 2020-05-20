#!/usr/bin/env python3

import speech_recognition as sr
from gtts import gTTS
import playsound
import os 
import subprocess as sb
#import threading as th
import re
def not_recognized():
    path=sb.getoutput('pwd')
    path=path+'/bin/audio/listening_failure.mp3'
    playsound.playsound(path)

def listen():
    path=sb.getoutput('pwd')
    url1=re.compile('www\.[a-z0-9]+\.[a-z.]+[.a-z]*')
    url2=re.compile('[a-z0-9]+\.[a-z.]+[.a-z]*')
    browser=str(sb.getoutput('xdg-mime query default `xdg-mime query filetype "$(find ~ / -iname *.html -print -quit)"`'))
    #browser=browser[:browser.index('.')]
    file=str(sb.getoutput('xdg-mime query default inode/directory'))
    #file=file[:file.index('.')]
    with sr.Microphone() as source:
        audio = r.listen(source,timeout=6,phrase_time_limit=6)
    try:
        text=str(r.recognize_google(audio))
        print(text)
        flag=0
        if re.search(url1,text)!=None: 
            browser=browser[:browser.index('.')]
            sb.Popen([browser,str(re.findall(url1,text)[0])])
        elif re.search(url2,text)!=None:
            browser=browser[:browser.index('.')]
            sb.Popen([browser,str(re.findall(url2,text)[0])])
        else:
            if 'open' in text:
                import open_app as oapp 
                oapp.recognize_app(text,path,browser,file,0)
            elif 'close' in text:
                import close_app as capp
                capp.close_app(text,path,browser,file)
            elif 'search' in text:
                browser=browser[:browser.index('.')]
                sb.Popen([browser,'https://www.google.com/search?q='+text[text.index('search')+7:]])
            else:
                import webscrap
                webscrap.start(text)
                
    except sr.UnknownValueError:
        print("I did't understand your voice")
        not_recognized()
    except sr.RequestError or sr.URLError:
        print('System is not connected to the internet')
        path=path+'/bin/audio/internet_error.mp3'
        playsound.playsound(path)
def start():
    path=sb.getoutput('pwd')
    print('Say something..')
    path=path+'/bin/audio/initial_msg.mp3'
    playsound.playsound(path)
    listen()
r = sr.Recognizer()
start()
'''
below code is still in progress
def trigger():
    print('Say hello or hi to start')
    with sr.Microphone() as source:
        audio = r.listen(source,timeout=6,phrase_time_limit=6)
    try:
        text=str(r.recognize_google(audio))
        print(text)
        if 'hello' or 'hi' in text.lower():
            start()
    except sr.UnknownValueError:
        pass
    except sr.RequestError or sr.URLError:
        print('System is not connected to the internet')
        path=sb.getoutput('pwd')
        path=path+'/bin/audio/internet_error.mp3'
        playsound.playsound(path)

r = sr.Recognizer()
while(True):
    trigger()
'''           

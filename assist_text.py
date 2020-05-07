#import speech_recognition as sr
#from gtts import gTTS
#import playsound as playsound
import os as os
import subprocess as sb
# import threading as th
import re


def listen():
    url1=re.compile('www\.[a-z0-9]+\.[a-z.]+[.a-z]*')
    url2=re.compile('[a-z0-9]+\.[a-z.]+[.a-z]*')
    browser=str(sb.getoutput('xdg-mime query default `xdg-mime query filetype "$(find ~ / -iname *.html -print -quit)"`'))
    text=input('What can I do for you? ')
    file=str(sb.getoutput('xdg-mime query default inode/directory'))
    path=sb.getoutput('pwd')+'/'
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
listen()

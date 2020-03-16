import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import subprocess as sb
# import threading as th
import re
import open_app as oapp 

def not_recognized():
    path=sb.getoutput('pwd')+'/bin/audio/listening_failure.mp3'
    playsound.playsound(path)


def listen():
    path=sb.getoutput('pwd')
    r = sr.Recognizer()
    url1=re.compile('www\.[a-z0-9]+\.[a-z.]+[.a-z]*')
    url2=re.compile('[a-z0-9]+\.[a-z.]+[.a-z]*')
    browser=str(sb.getoutput('xdg-mime query default `xdg-mime query filetype "$(find ~ / -iname *.html -print -quit)"`'))
    file=str(sb.getoutput('xdg-mime query default inode/directory'))
    with sr.Microphone() as source:
        audio = r.listen(source,timeout=5,phrase_time_limit=5)
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
                oapp.recognize_app(text,path,browser,file,0)
            elif 'close' in text:
                app=oapp.recognize_app(text,path,browser,file)
                print(app)
                temp=text[text.index('close')+6:]
                if app!=None:
                    if 'gnome' in app_name.split('-') or 'gnome' in app_name.split('.'): 
                        print('gnome-'+temp)
                        app='gnome-'+temp
                    elif 'cinnamon' in app_name.split('-') or 'gnome' in app_name.split('.'):
                        print('cinnamon-'+temp)
                        app='cinnamon-'+temp
                    os.system('pkill '+app[:app.index('.')])
                    print('Closing '+ temp)
                    g=gTTS(text='Closing '+ temp)
                    g.save('sample.mp3')
                    playsound.playsound('sample.mp3')
                    os.remove(path+'/sample.mp3')
                else:
                    g=gTTS(text='Assistant failed to open requested app')
                    print('App opening failed')
                    g.save('sample.mp3')
                    playsound.playsound('sample.mp3')
                    os.remove(path+'/sample.mp3')
            else:
                browser=browser[:browser.index('.')]
                sb.Popen([browser,'https://www.google.com/search?q='+text])
    except sr.UnknownValueError:
        print("I did't understand your voice")
        not_recognized()
    except sr.RequestError or sr.URLError:
        print('System is not connected to the internet or check your firewall configuration.')
        path=path+'/bin/audio/internet_error.mp3'
        playsound.playsound(path)

def start():
    print('Say something..')
    path=sb.getoutput('pwd')+'/bin/audio/initial_msg.mp3'
    playsound.playsound(path)
    listen()

start()

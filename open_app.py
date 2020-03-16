import subprocess as sb 
import re
from gtts import gTTS
import playsound 
import os

def open_app(temp,path,app_name):
    print('Opening '+ temp)
    g=gTTS(text='Opening '+ temp)
    g.save('sample.mp3')
    print(app_name)
    playsound.playsound('sample.mp3')
    os.remove(path+'/sample.mp3')
    try:
            sb.Popen(app_name[:app_name.index('.')])
    except:
        if app_name.count('.')>2:
            try:
                if 'gnome' in app_name.split('-') or 'gnome' in app_name.split('.'): 
                    print('gnome-'+temp)
                    sb.Popen('gnome-'+temp)
                elif 'cinnamon' in app_name.split('-') or 'gnome' in app_name.split('.'):
                    print('cinnamon-'+temp)
                    sb.Popen('cinnamon-'+temp)
            except:
                    g=gTTS(text='Assistant failed to open requested app')
                    print('App opening failed')
                    g.save('sample.mp3')
                    playsound.playsound('sample.mp3')
                    os.remove(path+'/sample.mp3')
        
def recognize_app(text,path,browser,file,indicator=1):
    flag=0
    try:
        if indicator!=1:
            sb.Popen(text[text.index('open')+5:].lower())
        else:
            raise Exception 
    except:
        if 'browser' in text:
            temp='your default browser'
            app=browser
            if indicator!=1:
                open_app(temp,path,browser)
        elif 'file' and 'manager' in text:
            temp='your default file manager'
            app=file
            if indicator!=1:
                open_app(temp,path,file)
        else:
            if indicator!=1:
                temp=text[text.index('open')+5:].lower()
            else:
                temp=text[text.index('close')+6:].lower()
            t=os.listdir('/usr/share/applications')
            for app_name in t:
                if flag==1:
                    break
                elif temp in map(str.lower,app_name.split('.')):
                    flag=1
                    app=app_name
                    if indicator!=1:
                        open_app(temp,path,app_name)
                    break
                elif temp in map(str.lower,app_name.split('-')):
                    flag=1
                    app=app_name
                    if indicator!=1:
                        open_app(temp,path,app_name)
                    break
                else:  
                    s=app_name.split('-')
                    for i in range(len(s)):
                        if temp in map(str.lower,s[i].split('.')):
                            flag=1
                            app=app_name
                            if indicator!=1:
                                open_app(temp,path,app_name)
                            break
                    if flag==0:
                        s=app_name.split('.')
                        for i in range(len(s)):
                            if temp in map(str.lower,s[i].split('-')):
                                app=app_name
                                flag=1
                                if indicator!=1:
                                    open_app(temp,path,app_name)
                                break
            if indicator!=1:                    
                if  flag==0:
                        search=re.compile('(.*)(\n)(.*)')
                        a=sb.getoutput('find /home/ -iname '+temp+' -print -quit')
                        file=file[:file.index('.')]
                        if re.search(search,a)==None:
                            sb.Popen([file,a])
                            flag=1
                        else:
                            a=re.findall(search,a)
                            sb.Popen([file,a[0][-1]])
                            flag=1
                if flag==0:
                        g=gTTS(text=temp+' is not installed on  your system')
                        print(temp+' is not installed on  your system')
                        g.save('sample.mp3')
                        playsound.playsound('sample.mp3')
                        os.remove(path+'/sample.mp3')
                        return None
        return app

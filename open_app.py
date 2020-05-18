import subprocess as sb 
import re
from gtts import gTTS
import playsound as playsound 
import os as os 
def alert(temp,app_name,path):
    print('Opening '+ temp)
    g=gTTS(text='Opening '+ temp)
    g.save('sample.mp3')
    print(app_name)
    playsound.playsound('sample.mp3')
    os.remove(path+'/sample.mp3')

def open_app(temp,path,app_name):
    try:
        sb.Popen(app_name[:app_name.index('.')])
        alert(temp,app_name,path)
    except:
        if app_name.count('.')>2:
            flag=0
            dashes=app_name.split('-')
            dots=app_name.split('.')
            try:
                if 'gnome' in dashes or 'gnome' in dots: 
                    print('gnome-'+temp)
                    sb.Popen('gnome-'+temp)
                elif 'cinnamon' in dashes or 'cinnamon' in dots:
                    print('cinnamon-'+temp)
                    sb.Popen('cinnamon-'+temp)
                else:
                    for i in  range(len(dots)):
                        try:
                            sb.Popen(dots[i].lower())
                            alert(temp,app_name,path)
                            flag=1
                            break
                        except:
                            pass
                if flag==0:
                    raise Exception
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
            temp=text[text.index('open')+5:].lower()
            sb.Popen(temp)
            alert(temp,temp+'.desktop',path)
        else:
            raise Exception 
    except:
        if 'browser' in text:
            temp='your default browser'
            app=browser
            if indicator!=1:
                open_app(temp,path,app)
                return
        elif 'file manager' in text or 'files' in text:
            temp='your default file manager'
            app=file
            if indicator!=1:
                open_app(temp,path,app)
                return
        elif 'text' and 'editor' in text:
             temp='your default text editor'
             text_editor=str(sb.getoutput('xdg-mime query default `xdg-mime query filetype "$(find ~ / -iname *.txt -print -quit)"`'))
             app=text_editor
             if indicator!=1:
                open_app(temp,path,app)
                return
        else:
            if indicator!=1:
                temp=text[text.index('open')+5:].lower()
                #alert(temp,temp,path)
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
                        return
                    break
                elif temp in map(str.lower,app_name.split('-')):
                    flag=1
                    app=app_name
                    if indicator!=1:
                        open_app(temp,path,app_name)
                        return
                    break
                else:  
                    s=app_name.split('-')
                    for i in range(len(s)):
                        if temp in map(str.lower,s[i].split('.')):
                            flag=1
                            app=app_name
                            if indicator!=1:
                                open_app(temp,path,app_name)
                                return                           
                            break
                    if flag==0:
                        s=app_name.split('.')
                        for i in range(len(s)):
                            if temp in map(str.lower,s[i].split('-')):
                                app=app_name
                                flag=1
                                if indicator!=1:      
                                    open_app(temp,path,app_name)
                                    return
                                break
            if indicator!=1:                    
                if  flag==0:
                    try:
                        search=re.compile('(.*)(\n)(.*)')
                        a=sb.getoutput('find /home/ -iname '+temp+' -print -quit')
                        file=file[:file.index('.')]
                        if re.search(search,a)==None:
                            alert(temp,file,path)
                            sb.Popen([file,a])
                            flag=1
                            return
                        else:
                            a=re.findall(search,a)
                            alert(temp,file,path)
                            sb.Popen([file,a[-1][-1]])
                            flag=1
                            return
                    except:
                        pass
                if flag==0:
                        g=gTTS(text=temp+' is not installed on  your system')
                        print(temp+' is not installed on  your system')
                        g.save('sample.mp3')
                        playsound.playsound('sample.mp3')
                        os.remove(path+'/sample.mp3')
                        return None
        return app

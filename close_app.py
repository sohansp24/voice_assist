import subprocess as sb
import open_app as oapp
import os as os
from gtts import gTTS
import playsound as playsound
def close_app(text,path,browser,file):
        flag=0
        app=oapp.recognize_app(text,path,browser,file)
        print(app)
        temp=text[text.index('close')+6:]
        if app!=None and sb.getoutput('man'+app[:app.index('.')]).split()[0]=='No':
            if 'gnome' in app.split('-') or 'gnome' in app.split('.'): 
                print('gnome-'+temp)
                app='gnome-'+temp+'.'
                flag=1
            elif 'cinnamon' in app.split('-') or 'cinnamon' in app.split('.'):
                print('cinnamon-'+temp)
                app='cinnamon-'+temp+'.'
                flag=1
            else:
                dots=app.split('.')
                for i in  range(len(dots)):
                    if sb.getoutput('man'+dots[i]).split()[0]!='No':
                            app=dots[i]+'.'
                            flag=1
                            break
                       
        else:
            flag=1
            print('Closing '+ temp)
            g=gTTS(text='Closing '+ temp)
            g.save('sample.mp3')
            playsound.playsound('sample.mp3')
            os.remove(path+'/sample.mp3')
            os.system('pkill '+app[:app.index('.')])
            
        if flag==0:
            g=gTTS(text='Assistant failed to close requested app')
            print('App closing failed')
            g.save('sample.mp3')
            playsound.playsound('sample.mp3')
            os.remove(path+'/sample.mp3')
            return
 

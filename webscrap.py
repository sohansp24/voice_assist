import urllib
import requests
from bs4 import BeautifulSoup
import webbrowser
from gtts import gTTS
import os
import playsound
language="en"
def speak(text):
    print(text)
    obj=gTTS(text=text,lang=language)
    filename="voice.mp3"
    obj.save(filename)
    playsound.playsound(filename)	
    os.remove('voice.mp3')
def start(query):
    #query=input('What do you want to find? ')
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"

    # desktop user-agent
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    # mobile user-agent
    MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

    headers = {"user-agent" : MOBILE_USER_AGENT}
    resp = requests.get(URL, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")

    #with open('output.html', 'wb') as f:
    #    f.write(response.content)
    #webbrowser.open('output.html')


    soup = BeautifulSoup(resp.text, 'lxml')
    #print(soup)
    response=''
    temp=soup.find_all(attrs={'class':'wob_t'})
    for g in temp:
        try:
            response='The temperature in your location is '+g.text+' degree celsius'
            break
        except:
            continue
        
    mean=soup.find_all(attrs={'class':'QIclbb'})
    for g in mean:
        try:
            response='meaning is '+g.text
            break
        except:
            continue

    desp=soup.find_all(attrs={'class':'kno-rdesc'})
    for g in desp:
        try:
            if(len(g)):
                response=g.find('span').text
        except:
            continue
            
    if(len(temp)>0 or len(mean)>0 or len(desp)>0):
        speak(response)

    else:
        webbrowser.open(URL, new=2)




import os
import threading
import subprocess as sb
import random
#import speech_recognition as sr
from nltk.stem import SnowballStemmer
list1=os.listdir('english')
list2=os.listdir('hindi')
list3=[list1,list2]
snowball=SnowballStemmer('english')
list_songs=[]
def fun(args):    
    sb.Popen(['celluloid',args])
def start_thread(song):
     t=threading.Thread(target=fun,args=(song,))
     t.start()
def play_song():
    x=random.randint(0,len(list3)-1)
    song=random.choice(list3[x])
    if x==0:
        song='english/'+song
    elif x==1:
        song='hindi/'+song
    list_songs.append(song)
    start_thread(song)
def play_hin_eng(string,list_):
    song=string+random.choice(list_)
    list_songs.append(song)
    start_thread(song)
while True:
    print('Say')
    string=input()
    s1=string.split()
    s=[]
    for x in s1:
        s.append(snowball.stem(x))
    if 'play' and 'english' in s:
        play_hin_eng('english/',list1)    
    elif 'play' and 'hindi' in s:
        play_hin_eng('hindi/',list2)  
    elif 'quit' in s or 'stop' in s:
        sb.getoutput('pkill celluloid')
        break
    elif 'restart' in s:
        start_thread(list_songs[len(list_songs)-1])
    elif 'previous' in s or 'earlier' in s:
        start_thread(list_songs[len(list_songs)-2])
    elif 'change' in s:
        play_song()
    else:
        play_song()    
        
        
    

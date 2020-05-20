import os
from playsound import playsound
import random
from nltk.stem import SnowballStemmer
snowball=SnowballStemmer('english')
string=input('Enter input:')
s1=string.split()
s=[]
for x in s1:
    s.append(snowball.stem(x))
list1=os.listdir('english')
list2=os.listdir('hindi')
list3=[list1,list2]
if 'play' and 'english' in s:
    song='english/'+random.choice(list1)
    playsound(song)
elif 'play' and 'hindi' in s:
    song='hindi/'+random.choice(list2)
    playsound(song) 
else:
    x=random.randint(0,len(list3)-1)
    song=random.choice(list3[x])
    if x==0:
        song='english/'+song
    elif x==1:
        song='hindi/'+song
    playsound(song)
        
        
    

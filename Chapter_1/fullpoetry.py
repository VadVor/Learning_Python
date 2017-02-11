# -*- coding: utf-8 -*-
import random 
article=["то","этак","как-бы","так",]
noun=["человек","кот","животное","собака",]
verb=["бежит","прыгнул","поплыл","летит",]
adverb=["плохой","тихий","мутный","спокойный",]

def note(): 
    x=random.randint(1,2)
    y1=random.choice(article)
    y2=random.choice(noun)
    y3=random.choice(verb)
    y4=random.choice(adverb)
    if x==1:
        print(y1,y2,y3,y4)
    else:
        print(y1,y2,y3)
i=1
while True:
    line=input("Введите число строк --> или (Enter (5 строк)): ")
    if line:
            z=int(line) 
            if 5< z <=10:
                while i <= int(line):
                    note()
                    i+=1
                    z+=1
            break
    else:
        while i <=5:
            note()
            i+=1
        break

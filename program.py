#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import csv, copy
import matplotlib
import datetime
from datetime import datetime
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#import pylab
#from pylab import figure, axes, pie, title, show

themes = ['0', 'Все', 'Алчность', 'Бабушки', 'Бесит', 'Бобмалейло', 'Бомжи', 'Великая Победа', 'Весна', 'Детство', 'Добро',  
'Дружба', 'Ебанько', 'Жестокость', 'Зависть', 'Зима', 'Иллюстрации', 'Кино', 'Коты', 'Лайфхак', 'Лень', 'Лето',  
'Любовь', 'Мечты', 'Мистика', 'Москва', 'Музыка', 'Наблюдения', 'Ненависть', 'Новый Год', 'Общение', 'Одиночество', 'Осень' 
'От редакции', 'Пиздец', 'Питер', 'Политика', 'Похоть', 'Пошлое', 'Предательство', 'Провал', 'Пьянь', 'Работа', 'Разное', 'Религия',
'Семья', 'Смешное', 'Сны', 'Собаки', 'Соседи', 'Странное', 'Страшное', 'Стыдно', 'Счастье', 'Успех', 'Фууу', 'Хобби', 'Чернуха']

print "Welcome to Overseen!"
print "As seen in Overheard, Russia's largest confessions portal"
choice = raw_input("Please reply 1 for detailed instructions, 2 to skip to word input")
if choice == '1':
    print "This database contains secrets from August 1 2013 to April 30 2016 for a total of 49780."
    print "Each secret falls into one of the following categories:"
    print "Russian (English) /number of secrets"
    print "------------------------------------"
    print 'Все (All categories) /49780' 
    print 'Алчность (Greed) /81'
    print 'Бабушки (Old ladies/Grandmas) /573' 
    print 'Бесит (Enraged) / 1231' 
    print 'Бобмалейло (Whoredom) /5' 
    print 'Бомжи (Homeless people) /145' 
    print 'Великая Победа (The Great Victory) /85' 
    print 'Весна (Spring) /72' 
    print 'Детство (Childhood) /2608'  
    print 'Добро (Kindness) /921'  
    print 'Дружба (Friendship) /570'  
    print 'Ебанько (Crazy/Stupid/Mental) /549'  
    print 'Жестокость (Cruelty) /358' 
    print 'Зависть (Envy) /142' 
    print 'Зима (Winter) /61'  
    print 'Иллюстрации (Illustrations) /0'  
    print 'Кино (Cinema) /0' 
    print 'Коты (Cats) /1087'
    print 'Лайфхак (Lifehack) /1413' 
    print 'Лень (Sloth) /302' 
    print 'Лето (Summer) /84'  
    print 'Любовь (Love) /732' 
    print 'Мечты (Dreams) /1193'  
    print 'Мистика (Mysticism) /289'  
    print 'Москва (Moscow) /30'  
    print 'Музыка (Music) /229' 
    print 'Наблюдения (Observations) /2751' 
    print 'Ненависть (Hatred) /334' 
    print 'Новый Год (New Year) /143' 
    print 'Общение (Communication) /11'  
    print 'Одиночество (Loneliness) /401' 
    print 'Осень (Autumn/Fall) /8' 
    print 'От редакции (From the editors) /40'  
    print 'Пиздец (Fucked up/Horrible) /755' 
    print 'Питер (St. Petersburg) /58' 
    print 'Политика (Politics) /28' 
    print 'Похоть (Lust) /497' 
    print 'Пошлое (Obscene) /1174' 
    print 'Предательство (Betrayal) /223' 
    print 'Провал (Failure) /2199' 
    print 'Пьянь (Drunkards) /392' 
    print 'Работа (Work) /1709'
    print 'Разное (Miscellaneous) /15897' 
    print 'Религия (Religion) /234'
    print 'Семья (Family) /2648'
    print 'Смешное (Funny) /775' 
    print 'Сны (Night dreams) /743' 
    print 'Собаки (Dogs) /0'  
    print 'Соседи (Neighbors) /152' 
    print 'Странное (Weird) /1504'
    print 'Страшное (Scary/Awful) /870' 
    print 'Стыдно (Embarassing/Shameful) /674'  
    print 'Счастье (Happiness) /483' 
    print 'Успех (Success) /571'
    print 'Фууу (Ewww) /438'
    print 'Хобби (Hobbies) /517'
    print 'Чернуха (Black, as in Black Humor) /191'
    print "We extracted all the 2113451 words from the secrets and tagged them by time so that you could see how each"
    print "word's frequency per million words changed over time."
    print "Choose one or two words and a category for each, and a name under which the plot should be saved."
    print "Use Google Translate to get the words in Russian, and please use lowercase characters. There is no stemming, so input the word in full."
    print "For example, see how \"love\" is represented in its category vs the category Miscellaneous or all secrets."
    print "It would make sense for either the words or the categories to be the same (cat in Cats and crazy in Stupid are not comparable)"
    print "Please allow the program to run for around 10 minutes for one word, around 15 minutes for two."
word = raw_input("Enter first word")
category = raw_input("Enter first category (Please input category exactly as it's given in Russian).")
while category not in themes:
    category = raw_input("Your input doesn't match the categories we have. Please try again")
print "Second word will only be included if both of the following two inputs are not 0"
word2 = raw_input("Enter second word (0 if none)")
category2 = raw_input("Enter second category (0 if no second word).")
while category2 not in themes:
    category2 = raw_input("Your input doesn't match the categories we have. Please try again")
filename = raw_input("Under which name would you like to save the plot? No extension please")
while filename == '':
    filename = raw_input("Please input something for the file name")

print "Thanks!"    
print "The author of this program suggests you go get some coffee, relax, maybe call a friend, and check back in 20 minutes."
print "She is sorry about this."
data = []
with open('words.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
f.close()
data.remove(data[0])
    
x = []
y = []
x2 = []
y2 = []
count = 1
count2 = 1
dnum = 1.0
dnum2 = 1.0
for d in data:
    if category == 'Все':
        if d[0] == word:
            x.append(datetime.strptime(d[1], "%Y-%m-%d %H:%M"))
            y.append(((count/dnum)*1000000))
            count += 1
    else:
        if d[2] == category:
            if d[0] == word:
                x.append(datetime.strptime(d[1], "%Y-%m-%d %H:%M"))
                y.append(((count/dnum)*1000000))
                count += 1
    print dnum
    dnum += 1
if (word2 != '0') and (category2 != '0'):  
    for d in data:
        if category2 == 'Все':
            if d[0] == word2:
                x2.append(datetime.strptime(d[1], "%Y-%m-%d %H:%M"))
                y2.append(((count2/dnum2)*1000000))
                count2 += 1
        else:
            if d[2] == category2:
                if d[0] == word2:
                    x2.append(datetime.strptime(d[1], "%Y-%m-%d %H:%M"))
                    y2.append(((count2/dnum2)*1000000))
                    count2 += 1
        print dnum2
        dnum2 += 1

    plt.plot(x, y, 'r', x2 , y2, 'g')

else: 
    plt.plot(x, y, 'r')
#plt.plot(x,y)
#plt.show()
file = filename + '.svg'
plt.savefig(file)
print "Looks like we're done! Check your working directory for the file, please."
print "The first word is in red, the second (if applicable) in green."
print "Thank you!"
print "Restart the program to do more things."
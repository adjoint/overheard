#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import csv, copy
import matplotlib
import datetime
from datetime import datetime
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import nltk
#import pylab
#from pylab import figure, axes, pie, title, show

themes = ['0', 'Все', 'Алчность', 'Бабушки', 'Бесит', 'Бобмалейло', 'Бомжи', 'Великая Победа', 'Весна', 'Детство', 'Добро',  
'Дружба', 'Ебанько', 'Жестокость', 'Зависть', 'Зима', 'Иллюстрации', 'Кино', 'Коты', 'Лайфхак', 'Лень', 'Лето',  
'Любовь', 'Мечты', 'Мистика', 'Москва', 'Музыка', 'Наблюдения', 'Ненависть', 'Новый Год', 'Общение', 'Одиночество', 'Осень' 
'От редакции', 'Пиздец', 'Питер', 'Политика', 'Похоть', 'Пошлое', 'Предательство', 'Провал', 'Пьянь', 'Работа', 'Разное', 'Религия',
'Семья', 'Смешное', 'Сны', 'Собаки', 'Соседи', 'Странное', 'Страшное', 'Стыдно', 'Счастье', 'Успех', 'Фууу', 'Хобби', 'Чернуха']

data = []
with open('words.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
f.close()
data.remove(data[0])
f = open('30mostcommonwordsbycategory-long.txt', 'w')
for category in themes:
    ctext = []
    for d in data:
       if (d[2] == category) and (len(d[0]) > 6): #gets words longer than three letters
           ctext.append(d[0])
    fdist1 = nltk.FreqDist(ctext)
    common = fdist1.most_common(30)
    f.write(category + '\n')
    for line in common:
        f.write(str(line[0]) + ', ' + str(line[1]) + '\n')
    f.write('\n')
    print category
    
f.close()













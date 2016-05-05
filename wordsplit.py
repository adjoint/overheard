#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import csv, copy
import networkx as nx
import matplotlib.pyplot as plt

data1 = []
data2 = []
data3 = []

with open('ideer(1).csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        data1.append(row)
f.close()
datacopy1 = copy.deepcopy(data1)
datacopy1.remove(datacopy1[0])

with open('ideer(2).csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        data2.append(row)
f.close()
datacopy2 = copy.deepcopy(data2)
datacopy2.remove(datacopy2[0])

with open('ideer(3).csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        data3.append(row)
f.close()
datacopy3 = copy.deepcopy(data3)
datacopy3.remove(datacopy3[0])
data = datacopy1 + datacopy2 + datacopy3
themes = []
for d in data:
    if d[1] not in themes:
        themes.append([d[1], 0])
k=1
for d in data:
    for t in themes:
        if d[1] == t[0]:
            t[1] += 1
            print k
            break
    print k
    k+=1
            
for t in themes:
    print str(t[0]) + ' ' + str(t[1]) + '\n'
info = []    
n = 0
data.reverse()
with open('words1.csv', 'w') as csvfile:
    fieldnames = ['word', 'time', 'category', 'number']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    
    for d in data:
        secret = d[3].split(' ')
        new = []
        for i in secret:
            k = i.split(',')
            new += k
        for word in new:
            newword = ''
            for j in word:
                if j not in ',.?!:-;()%$#^=\/{}[]№\'"':
                    newword += j
            if newword != '':
                writer.writerow({'word': str(newword), 'time': str(d[2]), 'category': str(d[1]), 'number': str(d[0])})
#            info.append([newword, d[2][:10], d[1], d[0]])
        print n
        n += 1
    
    
csvfile.close()

"""f = open('data.txt', 'w')
for a in info:
    f.write(str(a[0]) +', ' + str(a[1]) + ', ' + str(a[2]) + ', ' + str(a[3]) + '\n' )
f.close() """

    






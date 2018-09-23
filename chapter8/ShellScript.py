# -*- coding: utf-8 -*-



print "8.6 for语句"

print "8.6.1 一般语法"

print "8.6.2 用于序列类型"
for eachLetter in 'Names':
    print 'current letter: ', eachLetter

print "1 通过序列项迭代"
nameList = ['Walter', 'Nicole', 'Steven', 'Henry']
for eachName in nameList:
    print eachName, "Lim"

print "2 通过序列索引迭代"
nameList = ['Cathy', 'Terry', 'Joe', 'Heather', 'Lucy']
for nameIndex in range(len(nameList)):
    print "Liu, ", nameList[nameIndex]
print len(nameList)
print range(len(nameList))

print "3 使用项和索引迭代"
nameList = ['Donn', 'Shirley', 'Ben', 'Janice', 'David', 'Yen', 'Wendy']
for i, eachLee in enumerate(nameList):
    print "%d %s Lee" % (i + 1, eachLee)

print "8.6.4 range()内建函数"
print range(2, 19, 3)
print range(3, 7)
for eachVal in range(2, 19, 3):
    print "Value is: ", eachVal

print range(5)
for count in range(2, 5):
    print count

print "8.6.5 xrange()内建函数"

print "8.6.6 与序列相关的内建函数"
albums = ('Poe', 'Gaudi', 'Freud', 'Poe2')
years = (1976, 1987, 1990, 2003)
for album in sorted(albums):
    print album,
for album in reversed(albums):
    print album,
for i, album in enumerate(albums):
    print i, album
for album, yr in zip(albums, years):
    print yr, album

print "8.7 break语句"
print "8.8 continue语句"
print "8.9 pass语句"
print "8.10 再谈else语句"
print "8.11 迭代器和iter()函数"
print "8.11.4 使用迭代器"
print "1 序列"
myTuple = (123, 'xyz', 45.67)
i = iter(myTuple)
print i.next()
print i.next()
print i.next()
# print i.next()  # StopIteration

print "2 字典"
legends = {('Poe', 'author'): (1809, 1849, 1976),
           ('Gaudi', 'architect'): (1852, 1906, 1987),
           ('Frend', 'psychoanalyst'): (1856, 1939, 1990)}
for eachLegend in legends:
    print 'Name: %s \tOccupation: %s' % eachLegend
    print '    Birth: %s\tDeath: %s\tAlbum: %s\n' % legends[eachLegend]


print "3 文件"
myFile = open('config-win.txt')
for eachLine in myFile:
    print eachLine,  # comma suppresses extra \n
myFile.close()

print "8.11.5 可变对象和迭代器"
myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for eachKey in myDict:
    print eachKey, myDict[eachKey]
    # del myDict[eachKey]   # RuntimeError: dictionary changed size during iteration

print map(lambda x: x ** 2, range(6))
print [x ** 2 for x in range(6)]
seq = [11, 10, 9, 9, 10, 10, 9, 8, 23, 9, 7, 18, 12, 11, 12]
print filter(lambda x: x % 2, seq)
print [x for x in seq if x % 2]

print "1 矩阵样例"
print [(x+1, y+2) for x in range(3) for y in range(5)]

print "2 磁盘文件案例"
f = open('hhga.txt', 'r')
print len([word for line in f for word in line.split()])

import os
print os.stat('hhga.txt').st_size
f.seek(0)  # 回到文件头
print sum([len(word) for line in f for word in line.split()])


print "8.13 生成器表达式"

print "2 交叉配对样例"
rows = [1, 2, 3, 17]
def cols():
    yield 56
    yield 2
    yield 1

x_product_pairs = ((i, j) for i in rows for j in cols())

for pair in x_product_pairs:
    print pair

print "3 重构样例"
print max(len(x.strip()) for x in open('hhga.txt'))

# -*- coding: utf-8 -*-
import urllib

import operator

print "第6章 序列：字符串,列表和元组"
print "6.1 序列"
names = ('Faye', 'Leana', 'Daylen')
# print names[4]     # IndexError
print ('Faye', 'Leana', 'Daylen')[1]

s = 'abcdefgh'
print s[::-1]     # 可以视作翻转操作
print s[::2]      # 隔一个取一个的操作

print ('Faye', 'Leana', 'Daylen')[-100:100]

s = 'abcde'
i = -1
for i in range(-1, -len(s), -1):
    print s[:i]

print s[:0]

s = 'abcde'
for i in [None] + range(-1, -len(s), -1):
    print s[:i]

# basestring('foo')  #不能实例化抽象类basestring

print "6.2 字符串"

print "1 字符串的创建和赋值"
aString = 'Hello World!'
anotherString = "Python is cool!"
print aString
print anotherString
s = str(range(4))
print s

print "2 如何访问字符的值(字符和子串)"
print aString[0]
print aString[1:5]
print aString[6:]

print "3 如何改变字符串"
aString = aString[:6] + "Python!"
print aString
aString = "different string altogether"
print aString

print "4 如何删除一个字符串"
aString = 'Hello World!'
aString = aString[:3] + aString[4:]
print  aString
aString = ''   # 通过赋一个空字符串或者使用del语句来清空或者删除一个字符串
print aString
del aString

print "6.3 字符串和操作符"
print "6.3.1 标准类型操作符"
str1 = 'abc'
str2 = 'lmn'
str3 = 'xyz'
print str1 < str2  # 字符串是按照ASCII值的大小来比较的
print str2 != str3
print str1 < str3 and str2 == 'xyz'

print "6.3.2 序列操作符切片([]和[:])"
aString = 'abcd'
print len(aString)
print aString[0]
print aString[1:3]
print aString[2:4]
# print aString[4]  # IndexError: string index out range
print aString[-1]
print aString[-3:-1]
print aString[-4]

print aString[2:]  # 以最后一个索引值为结束索引
print aString[1:]  # 以最后一个索引值为结束索引
print aString[:-1]  # 以第一个索引值为开始索引
print aString[:]  # 以第一个索引值为开始索引, 以最后一个索引值为结束索引

print "1 成员操作符（in,not in）"
print 'bc' in 'abcd'
print 'n' in 'abcd'
print 'nm' in 'abcd'

import string
print string.uppercase
print string.lowercase
print string.letters
print string.digits
print string.hexdigits
print string.whitespace
print string.ascii_letters
print string.ascii_lowercase
print string.ascii_uppercase

print "2 连接符（+）"
print 'Spanish' + 'Inquisition'
print 'Spanish' + ' ' + 'Inquisition'
s = 'Spanish' + ' ' + 'Inquisition' + ' Made Easy'
print s
print  string.upper(s[:3] + s[20])

print '%s %s' % ('Spanish', 'Inquisition')
print ' '.join(('Spanish', 'Inquisition', 'Made Easy'))
print ('%s%s' % (s[:3], s[20])).upper()

print "3 编译时字符串连接"
foo = 'Hello' 'World!'
print foo
# f = urllib.urlopen('http://'                # protocol
#                    'localhost'              # hostname
#                    ':8000'                  # port
#                    'cgi-bin/friends2.py'    # file
#                    )

print 'http://' 'localhost' ':8000' 'cgi-bin/friends2.py'

print "4 普通字符串转化为Unicode字符串"
print 'Hello' + u' ' + 'World' + u'!'
print 'Ni!' * 3
print '*' * 4
print '-' * 20, 'Hello World!', '-' * 20
who = 'knights'
print who * 2
print who


print "6.4 只适用于字符串的操作符"
print "6.4.1 格式化操作符(%)"
print "1 十六进制输出"
print "%x" % 108
print "%X" % 108
print "%#X" % 108
print "%#x" % 108

print "2 浮点型和科学计数法形式输出"
print '%f' % 1234.567890
print '%.2f' % 1234.567890  # 四舍五入
print '%E' % 1234.567890
print '%g' % 1234.567890
print '%G' % 1234.567890
print '%e' % (1111111111111111111111L)

print "3 整型和字符串输出"
print "%+d" % 4
print "%+d" % -4
print "we are at %d%%" % 100
print "Your host is: %s" % 'earth'
print 'Host: %s\tPort: %d' % ('mars', 80)
num = 123
print 'dec: %d/oct: %#o/hex: %#X' % (num, num, num)
print 'MM/DD/YY = %02d/%2d/%d' % (2, 15, 67)
w, p = 'Web', 'page'
print 'http://xxx.yyy.zzz/%s/%s.html' % (w, p)
print 'There are %(howmany)d %(lang)s Quotation Symbols' % {'lang':'Python', 'howmany': 3}


print "6.4.2 字符串模板：更简单的替代品"
from string import Template
s = Template('There are ${howmany} ${lang} Quotation Symbols')
print s.substitute(lang='Python', howmany=3)
# print s.substitute(lang='Python')  # KeyError
print s.safe_substitute(lang='Python')

print "6.4.3 原始字符串操作符(r/R)"
print '\n'
print r'\n'
# f = open('C:\windows\temp\readme.txt', 'r')
# f = open(r'C:\windows\temp\readme.txt', 'r')

import re
m = re.search('\\[rtfvn]', r'Hello World!\n')
if m is not None:
    print m.group()
m = re.search(r'\\[rtfvn]', r'Hello World!\n')
if m is not None:
    print m.group()

print "Unicode字符串操作符(u/U)"
print u'abc'
print u'\u1234'
print u'abc\u1234\n'
print ur'Hello\nWorld!'

print "6.5 内建函数"
print "6.5.1 标准类型函数"
str1 = 'abc'
str2 = 'lmn'
str3 = 'xyz'
print cmp(str1, str2)
print cmp(str3, str1)
print cmp(str2, 'lmn')

print "6.5.2 序列类型函数"
str1 = 'abc'
print len(str1)
print len('Hello World!')

str2 = 'lmn'
str3 = 'xyz'
print max(str2)
print min(str3)
print min('ab12cd')
print min('AB12CD')
print min('ABabCDcd')
s = 'foobar'
for i, t in enumerate(s):
    print i, t

s, t = 'foa', 'obr'
print zip(s, t)

print "6.5.3 字符串类型函数"
# user_input = raw_input("Enter youer name: ")
# print user_input
# print len(user_input)

print isinstance(u'\0xAB', str)
print not isinstance('foo', unicode)
print isinstance(u'', basestring)
print not isinstance('foo', basestring)

print chr(65)
print ord('a')
print unichr(12345)
# print chr(12345)  # ValueError: chr() arg not in range(256)
# print ord(u'\ufffff')  # TypeError: ord() expected a character, but string of length 2 found
print ord(u'\u2345')

quest = 'what is your favorite color?'
print quest.capitalize()
print quest.center(40)
print quest.count('or')
print quest.endswith('blue')
print quest.endswith('color?')
print quest.find('or', 30)
print quest.find('or', 22)
print quest.index('or', 10)
print ':'.join(quest.split())
print quest.replace('favorite color', 'quest')
print quest.upper()
print quest.lower()
print quest.islower()
print quest.isupper()
print quest.isalnum()
print quest.isalpha()
print quest.isdigit()
print quest.isspace()
print quest.istitle()

print "6.11 列表"
print "1 如何创建列表类型数据并给它赋值"
aList = [123, 'abc', 4.56, ['inner', 'list'], 7-9j]
anotherList = [None, 'something to see here']
print aList
print anotherList
aListThatStatedEmpty = []
print aListThatStatedEmpty
print list('foo')

print "2 如何访问列表中的值"
print aList[0]
print aList[1:4]
print aList[:3]
print aList[3][1]

print "3 如何更新列表"
print aList
print aList[2]
aList[2] = 'float replacer'
print aList
anotherList.append("hi, i'm new here")
print anotherList
aListThatStatedEmpty.append('not empty anymore')
print aListThatStatedEmpty

print "4 如何删除列表中的元素或者列表(本身)"
print aList
del aList[1]
print aList
aList.remove(123)
print aList
del aList

print "6.12 操作符"
print "6.12.1 标准类型操作符"
list1 = ['abc', 123]
list2 = ['xyz', 789]
list3 = ['abc', 123]
print list1 < list2
print list2 < list3
print list2 > list3 and list1 == list3

print "6.12.2 序列类型操作符"
print "1 切片[]和[:]"
num_list = [43, -1.23, -2, 6.19e5]
str_list = ['jack', 'jumped', 'over', 'candlestick']
mixup_list = [4.10, [1, 'x'], 'beef', -1.9+6j]
print num_list[1]
print num_list[2:-1]
print num_list[1:]
print str_list[2]
print str_list[:2]
print mixup_list
print mixup_list[1]

print mixup_list[1][1]
mixup_list[1][1] = -64.875
print mixup_list

print num_list
num_list[2:4] = [16.0, -49]
print num_list
num_list[0] = [65535L, 2e30, 76.45-1.3j]
print num_list

print "成员关系操作(in, not in)"
print mixup_list
print 'beef' in mixup_list
print 'x' in mixup_list
print 'x' in mixup_list[1]
print num_list
print -49 in num_list
print 34 in num_list
print [65535L, 2e30, 76.45-1.3j] in num_list

print "3 连接操作符(+)"
print num_list + mixup_list
print str_list + num_list
# print num_list + 'new item'   # TypeError: can only concatenate list (not "str") to list
num_list.append('new item')
print num_list

print "4 重复操作符(*)"
print num_list * 2
print num_list * 3
hr = '-'
hr *= 30
print hr

print "6.12.3 列表类型操作符和列表解析"
print [i * 2 for i in [8, -2, 5]]
print [i for i in range(8) if i % 2 == 0]


print "6.13 内建函数"
print "6.13.1 标准类型函数"
list1, list2 = [123, 'xyz'], [456, 'abc']
print cmp(list1, list2)
print cmp(list2, list1)
list3 = list2 + [789]
print list3
print cmp(list2, list3)

print "6.13.2 序列类型函数"
print "1 len()"
print len(num_list)
print len(num_list * 2)

print "2 max()和min()"
print max(str_list)
print max(num_list)
print min(str_list)
print min(num_list)

print "3 sorted()和reversed()"
s = ['They', 'stamp', 'them', 'when', "they're", 'small']
for t in reversed(s):
    print t,
print
print sorted(s)

print "4 enumerate()和zip()"
albums = ['tales', 'robot', 'pyramid']
for i, album in enumerate(albums):
    print i, album

fn = ['ian', 'stuart', 'david']
ln = ['bairnson', 'elliott', 'paton']
for i, j in zip(fn, ln):
    print ('%s %s' % (i, j)).title()

print "5 sum()"
a = [6, 4, 5]
print reduce(operator.add, a)
print sum(a)
print sum(a, 5)
a = [6., 4., 5.]
print sum(a)

print "6 list()和tuple()"
aList = ['tao', 93, 99, 'time']
aTuple = tuple(aList)
print aList, aTuple
print aList == aTuple
anotherList = list(aTuple)
print aList == anotherList
print aList is anotherList
print [id(x) for x in aList, aTuple, anotherList]

print "6.14 列表类型的内建函数"
print dir(list)  # dir([])
music_media = [45]
print music_media
music_media.insert(0, 'compact disc')
print music_media
music_media.append('long playing record')
print music_media
music_media.insert(2, '8-track tape')
print music_media

print 'cassette' in music_media
print 'compact disc' in music_media
print music_media.index(45)
print music_media.index('8-track tape')
# print music_media.index('cassette')   # ValueError: 'cassette' is not in list
for eachMediaType in (45, '8-track tape', 'cassette'):
    if eachMediaType in music_media:
        print music_media.index(eachMediaType)

print music_media
music_media.sort()   # 将列表元素排序
print music_media
music_media.reverse()  # 将列表元素翻转
print music_media

new_media = ['24/96 digital audio disc', 'DVD Audio disc', 'Super Audio CD']
music_media.append(new_media)
print music_media

# motd = []
# motd.append('MSG OF THE　DAY')
# f = open('/etc/motd', 'r')
# motd.extend(f)
# f.close()
# print motd

print "6.15 列表的特殊特性"
print "用列表构建其他数据结构"







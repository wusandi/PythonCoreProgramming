# -*- coding: utf-8 -*-
import os
import sys

print  '第2章 快速入门'
print 'Hello World'
# os.system('pause')

print '2.1 程序输出, print语句及“Hello World！”'
myString = 'Hello World'
print myString
print "%s is number %d!" % ('Python', 1)
print >> sys.stderr, 'Fatal error: invalid input!'
logfile = open('tmp/mylog.txt', 'a')
print >> logfile, 'Fatal error: invalid input!'
logfile.close()

print '2.2 程序输入和raw_input()内建函数'
user = raw_input('Enter login name:')
print 'Your login is: ', user
num = raw_input('Now enter a number: ')
print 'Doubling your number : %d' % (int(num) * 2) #内建函数int()将数值字符串转换成整型值
help(raw_input)

print '2.3 注释'
# one comment
print 'Hello World!' # another comment
def foo():
    "This is a doc string"
    return True

print '2.4 操作符'
print -2 * 4 + 3 ** 2
print 2 < 4
print 2 == 4
print 2 > 4
print 6.2 <= 6
print 6.2 <= 6.2
print 6.2 <= 6.20001
print 2 < 4 and 2 == 4
print 2 > 4 or 2 < 4
print not 6.2 <= 6
print 3 < 4 < 5
print 3 < 4 and 4 < 5

print '2.5 变量和赋值'
counter = 0
miles = 1000.0
name = 'Bob'
counter = counter + 1
kilometers = 1.609 * miles
print '%f miles is the same as %f km' % (miles, kilometers)


print '2.6 数字'
print 1.1
import decimal
print decimal.Decimal('1.1')

print '2.7 字符串'
pystr = 'Python'
iscool = 'is cool!'
print pystr[0]
print pystr[2:5]
print iscool[:2]
print iscool[3:]
print iscool[-1]
print pystr + iscool
print pystr + ' ' + iscool
print pystr * 2
print '-' * 20

print '2.8 列表和元组'
aList = [1, 2, 3, 4]
print aList
print aList[0]
print aList[2:]
print aList[:3]
aList[1] = 5
print aList
aTuple = ('robots', 77, 93, 'try')
print aTuple
print aTuple[:3]
try:
    aTuple[1] = 5
except TypeError as e:
    print str(e.__class__) + ': '+ str(e)

print '2.9 字典'
aDict = {'host': 'earth'}
aDict['port'] = 80
print aDict
print aDict.keys()
print aDict['host']
for key in aDict:
    print key, aDict[key]

print '2.10 代码块及缩进对齐'
print '2.11 if语句' # 参见chapter8
print '2.12 while循环' # 参见chapter8
counter = 0
while counter < 3:
    print 'loop #%d' % counter
    counter += 1

print '2.13 for循环和range()内建函数'
print 'I like to use the Internet for:'
for item in ['e-mail', 'net-surfing', 'homework', 'chat']:
    print item  #输出到不同行
for item in ['e-mail', 'net-surfing', 'homework', 'chat']:
    print item, #输出到同一行
print
who = 'knights'
what = 'Ni!'
print 'We are the', who, 'who say', what, what, what, what
print 'We are the %s who say %s' % (who, ((what + ' ') * 4))
for eachNum in [0, 1, 2]:
    print eachNum
for eachNum in range(3):
    print eachNum
foo = 'abc'
for c in foo:
    print c
for i in range(len(foo)):
    print foo[i], '(%d)' % i
for i, ch in enumerate(foo):
    print ch, '(%d)' % i

print '2.14 列表解析'
squared = [x ** 2 for x in range(4)]
for i in squared:
    print i
sqdEven = [x ** 2 for x in range(8) if not x % 2]
for i in sqdEven:
    print i

print '2.15 文件和内建函数open(), file()' # 参见chapter9
print '2.16 错误和异常' # 参见chapter10
print '2.17 函数' # 参见chapter11


def addMe2Me(x):
    'apply + operation to argument'
    return (x + x)


print addMe2Me(4.25)
print addMe2Me(10)
print addMe2Me('Python')
print addMe2Me([-1, 'abc'])


def foo(debug=True):
    'determine if in debug mode with default argument'
    if debug:
        print 'in debug mode'
    print 'done'

foo()
foo(False)

print '2.18 类' #第13章将详细介绍Python类和实例


class FooClass(object):
    """my very first class: FooClass"""
    version = 0.1       # class (data) attribute

    def __init__(self, nm='John Doe'):
        """constructor"""
        self.name = nm     #class instance (data) attribute
        print 'Created a class instance for', nm

    def showname(self):
        """display instance attribute and class name"""
        print 'Your name is', self.name
        print 'My name is', self.__class__.__name__

    def showver(self):
        """display class(static) attribute"""
        print self.version      # reference FooClass.version

    def addMe2Me(self, x):
        """apply + operation to argument"""
        return x + x

foo1 = FooClass()
foo1.showname()
foo1.showver()
print foo1.addMe2Me(5)
print foo1.addMe2Me('xyz')
foo2 = FooClass('Jane Smith')
foo2.showname()






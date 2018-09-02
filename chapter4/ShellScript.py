# -*- coding: utf-8 -*-

print '第4章 Python对象'

print '4.3 其它内建类型'
print type(42)
print type(type(42))

print '4.4 内部类型'
foostr = 'abcde'
print foostr[::-1]
print foostr[::-2]
foolist = [123, 'xba', 342.23, 'abc']
print foolist[::-1]

print '4.5 标准类型操作符'
print 2 == 2
print 2.46 <= 8.33
# print 5+4j >= 2-3j # 复数类型不能使用>= > < <=进行比较，书中讲的是错误的
print 'abc' == 'xyz'
print 'abc' > 'xyz'
print 'abc' < 'xyz'
print [3, 'abc'] == ['abc', 3]
print [3, 'abc'] == [3, 'abc']
print 3 < 4 < 7     # same as (3 < 4) and (4 < 7)
print 4 > 3 == 3    # same as (4 > 3) and (3 == 3)
print 4 < 3 < 5 != 2 < 7

a = [5, 'hat', -9.3]
b = a
print a is b
print a is not b
b = 2.5e-5
print a is b
print a is not b

x, y = 3.1414926536, -1024
print x < 5.0
print not (x < 5.0)
print (x < 5.0) or (y > 2.718281828)
print (x < 5.0) and (y > 2.718281828)
print not (x is y)

print '标准类型内建函数'
print type(4)
print type('Hello World')
print type(type(4))

a, b = -4, 12
print cmp(a, b)
print cmp(b, a)
b = -4
print cmp(a, b)
a, b = 'abc', 'xyz'
print cmp(a, b)
print cmp(b, a)
b = 'xyz'
print cmp(a, b)


print str(4.53-2j)
print str(1)
print str(2e10)
print str([0, 5, 9, 9])
print repr([0, 5, 9, 9])
print `([0, 5, 9, 9])`      # Python社区已经不再鼓励使用··操作符了
# print eval(`type(type)`)    # 不是所有repr返回的字符串都能够用eval内建函数得到原来的对象

print type('')
s = 'xyz'
print type(s)
print type(100)
print type(0+0j)
print type(0L)
print type(0.0)
print type([])
print type(())
print type({})
print type(type)
class Foo: pass     # new-style class
foo = Foo()
class Bar(object): pass # nwe-style class
bar = Bar()
print type(Foo)
print type(foo)
print type(Bar)
print type(bar)


print '标准类型的分类'
x = 'Python numbers and strings'
print id(x)
x = 'are immutable?!? What gives?'
print id(x)
i = 0
print id(i)
i = i + 1
print id(i)

aList = ['ammonia', 83, 85, 'lady']
print aList
print aList[2]
print id(aList)
aList[2] = aList[2] + 1
aList[3] = 'stereo'
print aList
print id(aList)
aList.append('gaudy')
aList.append(aList[2] + 1)
print id(aList)







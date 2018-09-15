# -*- coding: utf-8 -*-

print "第7章 影像和集合类型"

print "7.1 映射类型：字典"

print "7.1.1 如何创建字典和给字典赋值"
dict1 = {}
dict2 = {'name': 'earth', 'port': 80}
print dict1, dict2

fdict = dict((['x', 1], ['y', 2]))
print fdict

ddict = {}.fromkeys(('x', 'y'), -1)
print ddict

edict = {}.fromkeys(('foo', 'bar'))
print edict


print "7.1.2 如何访问字典中的值"
dict2 = {'name': 'earth', 'port': 80}
for key in dict2:
    print 'key=%s, value=%s' % (key, dict2[key])

print dict2['name']
print 'host %s is runing on port %d' % (dict2['name'], dict2['port'])

# print dict2['server']  # KeyError: 'server'

print 'server' in dict2  # or dict2.has_key('server')
print 'name' in dict2  # or dict.has_key('name')
print dict2['name']

dict3 = {}
dict3[1] = 'abc'
dict3['1'] = 3.14159
dict3[3.2] = 'xyz'
print dict3

print "7.1.3 如何更新字典"
dict2['name'] = 'venus'  # 更新已有条目
dict2['port'] = 6969     # 更新已有条目
dict2['arch'] = 'sunos5' # 增加新条目
print "host %(name)s is running on port %(port)d" % dict2

print "7.1.4 如何删除字典元素和字典"
del dict2['name']
dict2.clear()
del dict2

print "7.2 映射类型操作符"
print "7.2.1 标准类型操作符"
dict4 = {'abc': 123}
dict5 = {'abc': 456}
dict6 = {'abc': 123, 98.6:37}
dict7 = {'xyz': 123}
print dict4 < dict5
print (dict4 < dict6) and (dict4 < dict7)
print (dict5 < dict6) and (dict5 < dict7)
print dict6 < dict7

print "7.2.2 映射类型操作符"

print "7.3 映射类型的内建函数和工厂函数"
print "7.3.1 标准类型函数[type(),str(),cmp()]"
print "字典比较算法"
dict1 = {}
dict2 = {'host': 'earth', 'port': 80}
print cmp(dict1, dict2)
dict1['host'] = 'earth'
print cmp(dict1, dict2)

dict1['port'] = 8080
print cmp(dict1, dict2)
dict1['port'] = 80
print cmp(dict1, dict2)

dict1['prot'] = 'tcp'
print cmp(dict1, dict2)

dict2['prot'] = 'udp'
print cmp(dict1, dict2)

cdict = {'fruits': 1}
ddict = {'fruits': 1}
print cmp(cdict, ddict)
cdict['oranges'] = 0
ddict['apples'] = 0
print cmp(cdict, ddict)

print "7.3.2 映射类型相关的函数"
print dict(zip(('x', 'y'), (1, 2)))
print dict([['x', 1], ['y', 2]])
print dict([('xy'[i-1], i) for i in range(1, 3)])
print dict(x=1, y=2)
dict8 = dict(x=1, y=2)
print dict8
dict9 = dict(**dict8)
print dict9

dict9 = dict8.copy()
print dict9

dict2 = {'name': 'earth', 'port': 80}
print dict2
print len(dict2)

# hash([])  # TypeError: unhashable type: 'list'
# dict2[{}] = 'foo'  # TypeError: unhashable type: 'dict'


print "7.4 映射类型内建方法"
print dict2.keys()
print dict2.values()
print dict2.items()
for eachKey in dict2.keys():
    print 'dict2 key', eachKey, 'has value', dict2[eachKey]

for eachKey in sorted(dict2):
    print 'dict2 key', eachKey, 'has value', dict2[eachKey]


dict2 = {'host': 'earth', 'port': 80}
dict3 = {'host': 'venus', 'server': 'http'}
dict2.update(dict3)
print dict2
dict3.clear()
print dict3

dict4 = dict2.copy()
print dict4
print dict4.get('host')
print dict4.get('xxx')
print type(dict4.get('xxx'))
print dict4.get('xxx', 'no such key')


myDict = {'host': 'earth', 'port': 80}
print myDict.keys()
print myDict.items()
myDict.setdefault('port', 8080)
myDict.setdefault('prot', 'tcp')
print myDict.items()

print {}.fromkeys('xyz')
print {}.fromkeys(('love', 'honor'), True)

print "7.5 字典的键"
print "7.5.1 不允许一个键对应多个值"
dict1 = {'foo': 789, 'foo': 'xyz'}  # 从左到右检查键-值对, 如果不存在, 则添加, 否则替换
print dict1

dict1['foo'] = 123
print dict1

print "7.5.2 键必须是可哈希的"


print "7.6 集合类型"
print "7.6.1 如何创建集合类型和给集合赋值"
s = set('cheeseshop')
print s
t = frozenset('bookshop')
print t
print type(s)
print type(t)
print len(s)
print len(t)
print len(s) == len(t)
print s == t

print "7.6.2 如何访问集合中的值"
print 'k' in s
print 'k' in t
print 'c' not in t
for i in s:
    print i

print "7.6.3 如何更新集合"
s.add('z')
print s
s.update('pypi')
print s
s.remove('z')
print s
s -= set('pypi')
print s

# t.add('z')  # AttributeError: 'frozenset' object has no attribute 'add'

print "7.6.4 如何删除集合中的成员和集合"
del s

print "7.7 集合类型操作符"
print "7.7.1 标准类型操作符(所有的集合类型)"
print "1 成员关系(in, not in)"
s = set('cheeseshop')
t = frozenset('bookshop')
print 'k' in s
print 'k' in t
print 'c' not in t

print "2 集合等价/不等价"
print s == t
print s != t
u = frozenset(s)
print s == u
print set('posh') == set('shop')

print "3 子集/超集"
print set('shop') < set('cheeseshop')
print set('bookshop') >= set('shop')

print "7.7.2 集合类型操作符(所有的集合类型)"
print "1 联合(|)"
print s | t

print "2 交集(&)"
print s & t

print "3 差补/相对补集(-)"
print s - t

print "4 对称差分(^)"
print s ^ t

print "5 混合集合类型操作"
print t | s
print t ^ s
print t - s
# v = s + t  # TypeError: unsupported operand type(s) for +: 'set' and 'frozenset'
v = s | t
print v
print len(v)
print s < v

print "7.7.3 集合类型操作符"
print "(Union)Update(|=)"
s = set('cheeseshop')
u = frozenset(s)
s |= set('pypi')
print s

print "Retention/Intersection Update(&=)"
s = set(u)
print s
s &= set('shop')
print s

print "Difference Update(-=)"
s = set(u)
s -= set('shop')
print s

print "Symmetric Difference Update(^=)"
s = set(u)
t = frozenset('bookshop')
s ^= t
print s

print "7.8 内建函数"
print "7.8.1 标准类型函数"
s = set(u)
print s
print len(s)

print "7.8.2 集合类型工厂函数"
print set()
print set([])
print set(())
print set('shop')
print set(['foo', 'bar'])
f = open('numbers', 'w')
for i in range(5):
    f.write('%d\n' % i)
f.close()

f = open('numbers', 'r')
print set(f)









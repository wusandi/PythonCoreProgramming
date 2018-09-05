# -*- coding: utf-8 -*-
from __future__ import division

print '第5章 数字'

print '数字简介'
anInt = 1
aLong = -9999999999999999999999L
aFloat = 3.141592653589732384626433832795
aComplex = 1.23+4.56j

anInt += 1
aFloat = 2.718281828

del anInt
del aLong, aFloat, aComplex

print '5.2 整型'
print 9999 ** 8
print 2 << 32

print '5.4 复数'
# 复数的内建属性
aComplex = -8.333-1.47j
print aComplex.real
print aComplex.imag
print aComplex.conjugate()

# 混合模式操作符
print 1 + 4.5

# 标准类型操作符
print 5.2 == 5.2
print -719 >= 833
# print 5+4e >= 2-3e
print 2 < 5 < 9
print 77 > 66 == 66
print 0. < -90.4 < 55.3e2 != 3 < 181
print (-1 < 1) or (1 < -1)

# 算术操作符
# 传统除法
print 1 / 2
print 1.0 / 2.0
# 真正的除法
print 1 / 2
print 1.0 / 2.0
# 地板除
print 1 // 2
print 1.0 // 2.0
print -1 // 2

print 3 ** 2
print -3 ** 2
print (-3) ** 2
print 4.0 ** -1.0
print 4 ** -1

print -442 - 77
print 4 ** 3
print 4.2 ** 3.2
print 8 / 3
print 8 % 3
print (60. - 32.) * (5. * 9.)
print 14 * 0x04
print 0170 * 4
print 0x80 + 0777
print 45L * 22L
print 16399L + 0xA94E8L
print -2147483648L - 52147483648L
print 64.375+1j + 4.23-8.5j
print 0+1j ** 2
print 1+1j ** 2
print (1+1j) ** 2
# 位操作符（只适用于整型）
print 30 & 45
print 30 | 45
print 45 & 60
print 45 | 60
print ~30
print ~45
print 45 << 1
print 60 >> 2
print 30 ^ 45

# 标准类型函数
print cmp(-6, 2)
print cmp(-4.333333, -2.718281828)
print cmp(0xFF, 255)
print str(0xFF)
print str(55.3e2)
print type(0xFF)
print type(98765432109876543210L)
print type(2-1j)

# 数字类型函数
## 转换工厂函数
print int(4.25555)
print long(42)
print float(4)
print complex(4)
print complex(2.4, -8)
print complex(2.3e-10, 45.3e4)

# 功能函数
print abs(-1)
print abs(10.)
print abs(1.2-2.1j)
print abs(0.23 - 0.78)

print coerce(1, 2)
print coerce(1.3, 134L)
print coerce(1, 134L)
print coerce(1j, 134L)
print coerce(1.23-41j, 134L)

print divmod(10, 3)
print divmod(3, 10)
print divmod(10, 2.5)
print divmod(2.5, 10)
print divmod(2+1j, 0.5-1j)

print pow(2, 5)
print pow(5, 2)
print pow(3.141592, 2)
print pow(1+1j, 3)

print round(3)
print round(3.45)
print round(3.4999999)
print round(3.4999999, 1)    # 精确到小数点后1位

import math
for eachNum in range(10):
    print round(math.pi, eachNum)

for eachNum in (.2, .7, 1.2, 1.7, -.2, -.7, -1.2, -1.7):
    print "int(%.1f)\t%+.1f" % (eachNum, float(int(eachNum)))
    print "floor(%.1f)\t%+.1f" % (eachNum, math.floor(eachNum))
    print "round(%.1f)\t%+.1f" % (eachNum, round(eachNum))
    print '-' * 20

# 进制转换函数
print hex(255)
print hex(230948231L)
print hex(65535 * 2)
print oct(255)
print oct(230948231L)
print oct(65535 * 2)

# ASCII转换函数
print ord('a')
print ord('A')
print ord('c')
print chr(97)
print chr(65L)
print chr(48)

# 布尔数
print bool(1)
print bool(True)
print bool(0)
print bool('1')
print bool('0')
print bool([])
print bool((1,))

foo = 42
bar = foo < 100
print bar
print bar + 100
print '%s' % bar
print '%d' % bar

class C: pass
c = C()
print bool(c)
print bool(C)


class C:
    def __nonzero__(self):
        return False

c = C()
print bool(c)
print bool(C)

True, False = False, True
print bool(True)
print bool(False)
False, True = True, False
print bool(True)
print bool(False)

# 十进制浮点型
print 0.1
from decimal import Decimal
dec = Decimal('.1')
print dec
# print dec + 1.0
print dec + Decimal('1.0')




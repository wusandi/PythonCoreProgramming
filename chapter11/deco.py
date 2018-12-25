
from time import ctime, sleep


def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()

    return wrappedFunc   # 注意这里返回的是一个函数


@tsfunc
def foo():
    pass


foo()   # 相当于调用了tsfunc(foo)()
sleep(4)

for i in range(2):
    sleep(1)
    foo()

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def add(x, y):  # 普通的传参
    """传进来的第一个参数就是x,第二个参数就是y"""
    print "x=%s,y=%s" % (x, y)
    return x+y


def power(base, exponent=2):  # 默认参数,没有默认值的参数一定要写在前面
    """调用的时候,base一定要传进来.
exponent可以传或者不传. 不传的时候, exponent就是2"""
    return base ** exponent


def request(host, port=80, path="/"):  # 再来一个
    return '%s:%s%s' % (host, port, path)

print add(10, 20)
print add(y=10, x=20)
print power(10)
print power(10, 3)
print request('www.ctrip.com')
print request('www.ctrip.com', path="/login")


print "="*20, "我是分割线, args,kargs", "="*20


def mysum(scale, *args):  # args
    return sum(args)*scale

# 感受一下
print mysum(2, 1, 2, 3, 4, 5)
print mysum(2, *range(5))


def f(**kargs):  # kargs
    print type(kargs)
    print kargs

# 想不到合适的例子, 简单感受下
f(x=1, y=2, z=3)
d = dict(x=1, y=2, z=3)
f(**d)


def f(scale, *args, **kargs):  # args, kargs混合的
    print scale
    print args
    print kargs

f(1, *range(5), **d)


print "="*20, "我是分割线, 默认值+args", "="*20
# 有默认值的参数要放在后在, 但是,
# args前面的参数也可以有默认值, 但好像没有意义?


def mysum(scale=2, *args):  # 希望是求和,并默认对结果乘2
    return sum(args)*scale

# 但实际上起不到这个效果
mysum(2, 1, 2, 3, 4)
mysum(1, 2, 3, 4)

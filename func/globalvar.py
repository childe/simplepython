#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 局部变量
l = range(3)
print l


def f():
    l = range(4)
    print l

f()
print l  # [0, 1, 2].  l并没有变化.

print "="*20, "我来分割, 下面的全局变量", "="*20

# 全局变量
l = range(3)
print l


def f():
    global l  # 这里指明了l是一个全局变量, 它就是函数外面定义的那个l
    l = range(4)
    print l

f()
print l  # [0, 1, 2, 3].  函数里面改变了函数外面的l.

print "="*20, "函数里面没有用global指明, 但还是影响了外面的变量"
l = range(3)
def f():
    print l
    l.append(4)
    print l
f()
print l  # [0, 1, 2, 3].  函数里面改变了函数外面的l.

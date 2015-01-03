#!/usr/bin/env python
# -*- coding: utf-8 -*-


class A(object):

    def __init__(self):
        print "init in A"
        self.a = 2

    def f1(self):
        print "f1 defined in A"

    def f2(self):
        print "f2 defined in A"


class B(A):

    def f1(self):
        print "f1 defined in B"


class C(object):

    def __init__(self):
        print "init in C"
        self.a = 2
        self.b = 3

    def f2(self):
        print "f1 defined in C"


class D(B, C):

    def f1(self):
        print "f1 defined in D"

d = D()
# 自己定义的直接调用,而且不会调用到父类方法
d.f1()

# 自己没有定义的, 深度递归向上寻找
d.f2()
print d.a

# 没有调用到C.__init__, 所居有d没有b这个属性, 会抛异常
print d.b

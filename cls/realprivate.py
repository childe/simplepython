#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""两个__打头, 其实并不是真正的private属性/方法"""

class Person(object):
    def __init__(self):
        self.__a = 1

    def __func1(self):
        print "func 1"

    def __func2(self):
        print "func 2"

    def public_api(self):
        self.__func1()
        self.__func2()
        print "done"

p = Person()
p.public_api()

print "="*20,"不可以直接调用"
try:
    print p.__a
except Exception as e:
    print e

try:
    p.__func1()
except Exception as e:
    print e

print "="*20,"还是可以通过下面方式调用"
print p._Person__a
p._Person__func1()

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person(object):

    """定义一个类:Person. 有名字, 年龄, 性别三个属性.
有个introduce方法, 用来介绍自己"""

    def __init__(self, name, age, gender):
        print "now init a object"
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print 'my name is %s, %s, %d years old' % (self.name, self.gender, self.age)

    def __del__(self):
        print "now destroy a object"


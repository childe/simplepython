#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person(object):

    """定义一个类:Person. 有名字, 年龄, 性别三个属性."""

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print 'my name is %s, %s, %d years old' % (self.name, self.gender, self.age)

p = Person("liujia", 28, u"男")
print p  # <__main__.Person object at 0x1004a7210>
p.introduce()  # my name is liujia, 男, 28 years old

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person(object):

    """定义一个类:Person. 有名字, 年龄, 性别三个属性.
有个introduce方法, 用来介绍自己"""

    count = 0  # 定义了一个类属性. 它不在任何方法中定义, 不是self.XXX.

    def __init__(self, name, age, gender):
        print "now init a Person."
        Person.count += 1  # 这样调用类属性
        print "There is %d persons" % Person.count
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print 'my name is %s, %s, %d years old' % (self.name, self.gender, self.age)

    def __del__(self):
        print "now destroy a object"
        Person.count -= 1  # 这样调用类属性
        print "There is %d persons" % Person.count

    @classmethod
    def howmany_persons(cls):
        return cls.count

p = Person("liujia", 28, u"男")
p2 = Person("zn", 29, u"男")
p.introduce()  # my name is liujia, 男, 28 years old
p2.introduce()  # my name is liujia, 男, 28 years old
del p
del p2

print
print "now there is %d persons" % Person.count
print "now there is %d persons" % Person.howmany_persons()

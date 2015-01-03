#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person(object):

    """定义一个类:Person. 有名字, 年龄, 性别三个属性.
有个introduce方法, 用来介绍自己"""

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print 'my name is %s, %s, %d years old' % (self.name, self.gender, self.age)

    def tell_carrer(self):
        """先占位一个方法, 意在说明子类中会实现这个方法.
        但不允许从Person实例中调用"""
        raise NotImplemented


class Teacher(Person):

    def __init__(self, name, age, gender, salary):
        super(Teacher, self).__init__(name, age, gender)
        self.salary = salary

    def introduce(self):
        super(Teacher, self).introduce()
        print "and my salary is %d" % self.salary

    def tell_carrer(self):
        print 'i am a teacher'

t = Teacher("Teacher1", 28, u"男", 10000)
print t
t.introduce()

# Teacher是Person的子类
print  issubclass(Teacher, Person)
print  issubclass(type(t), Person)

p = Person("liujia", 28, u"男")
# 下面的调用会招聘异常
p.tell_carrer()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 内存中创建了一个字典对象, 并把d1指向这块内存
d1 = {1: 1, 2: 4}

# d2和d1是同一个东西, 他们指向同一块内存, 就是引用的概念. d2是d1的引用, 其实也可以反过来说, d1是d2的引用.
d2 = d1
print "id(d1):", id(d1)
print "id(d2):", id(d2)
print id(d1) == id(d2)  # True


print "="*20, "del d1[1]",  "="*20
del d1[1]  # 在这块内存上进行数据操作, 是个self update. d1 d2还是指向这块内存.
print "d2:", d2
print "id(d1):", id(d1)
print "id(d2):", id(d2)
print id(d1) == id(d2)  # True


print "="*20, "对d1新赋值",  "="*20
d1 = {}  # 在内存中重新生成一个空字典对象, 把d1指向这块内存
print "d2:", d2
print "id(d1):", id(d1)  # d1的地址变化了
print "id(d2):", id(d2)  # d2还是指向原来的地址
print id(d1) == id(d2)  # False

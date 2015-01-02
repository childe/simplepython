#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "all operations of a tuple:"
#count, index
print ", ".join([e for e in dir(tuple) if not e.startswith('_')])


#==================== 定义 ====================
t = tuple()
t = ()
print type(t), t, len(t)  # <type 'tuple'> () 0

t = (1, 2)
print type(t), t  # <type 'tuple'> (1, 2)

t = 1, 2
print type(t), t  # <type 'tuple'> (1, 2)

# 注意,只有一个元素的话, 后面一定要加逗号
t = (1)
print type(t)  # <type 'int'>
t = (1,)
print type(t)  # <type 'tuple'>
t = 1,
print type(t)  # <type 'tuple'>

#==================== 将元组中的元素依次赋值 ====================
t = (1, 2, 3)
a, b, c = t
print a, b, c  # 1 2 3

#==================== 切片遍历和列表一样 ====================
pass

#==================== 元素不可改变 ====================
t = (1, 2, 3, 4)
t[0] = -1
"""Traceback (most recent call last):
  File "t.py", line 20, in <module>
    t[0] = -1
TypeError: 'tuple' object does not support item assignment
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "all operations of a tuple:"
#count, index
print ", ".join([e for e in dir(tuple) if not e.startswith('_')])


#==================== 定义 ====================
t = tuple()
t = ()
print type(t), t  # <type 'tuple'> ()


#==================== 切片遍历和列表一样 ====================
pass

#==================== 元素不可改变 ====================
t = (1,2,3,4)
t[0] = -1
"""Traceback (most recent call last):
  File "t.py", line 20, in <module>
    t[0] = -1
TypeError: 'tuple' object does not support item assignment
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 整数
a = 5
b = 6

print a, b

a = a+1
print a  # 6

a += 2
print a  # 8

print a**2  # 64
print a  # 8

a **= 2
print a  # 64

print a/b  # 10. notice!
print a % b  # 4
print divmod(a, b)  # 10 4

# 浮点数
f = 100.123
pi = 3.14
print f/pi  # 31.8863057325
print f//pi  # 31.0

# 自动向高精度靠齐
print type(a/b)  # <type 'int'>
print type(a+b)  # <type 'int'>
print type(a/f)  # <type 'float'>
print type(a+f)  # <type 'float'>

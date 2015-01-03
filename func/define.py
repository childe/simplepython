#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 定义,传参,返回值
print "="*20,"我是分割线","="*20
def add(x, y):
    """define一个函数,叫add, 需要两个参数x和y.
    这里只是定义,并不会执行."""
    return x+y

rst = add(10, 20)  # 这里函数执行
print rst


# 没有明确的返回值, 其实是返回了None
print "="*20,"我是分割线","="*20
def hello():
    print "hello, python"

rst = hello()
print rst is None #True

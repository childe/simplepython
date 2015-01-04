#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    print "="*20, "数字",  "="*20
    x = 10
    y = 10
    print "id(x):", id(x)
    print "id(y):", id(y)
    print x is y

    print "="*20, "字符串",  "="*20
    x = 10
    x ="abcd"
    y ="abcd"
    print "id(x):", id(x)
    print "id(y):", id(y)
    print x is y

    print "="*20, "数组字典等数据结构",  "="*20
    d1 = {1: 1, 2: 4}
    d2 = {1: 1, 2: 4}
    print "id(d1):", id(d1)
    print "id(d2):", id(d2)
    print d2 == d1  # True
    print d2 is d1  # False

    d2 = d1
    print "id(d1):", id(d1)
    print "id(d2):", id(d2)
    print d2 == d1  # True
    print d2 is d1  # False

    del d1[1]
    print d2

    d1 = {}
    print "id(d1):", id(d1)  # changed
    print "id(d2):", id(d2)  # not changed

if __name__ == '__main__':
    main()

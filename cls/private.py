#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person(object):

    def _func1(self):
        print "func 1"

    def _func2(self):
        print "func 2"

    def public_api(self):
        self._func1()
        self._func2()
        print "done"

p = Person()
p.public_api()

# 私有方法仍然成功调用了...
# 私有方法只是个概念,并不像C++强制不能外部调用.
p._func1()

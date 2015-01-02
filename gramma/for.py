#!/usr/bin/env python
# -*- coding: utf-8 -*-
print '*' * 20, "if", '*' * 20
for i in range(10):
    print i


print '*' * 20, "break", '*' * 20
for i in range(10):
    print i
    if i > 5:
        break


print '*' * 20, "continue", '*' * 20
for i in range(10):
    if i < 5:
        continue
    print i


# 没有break, 会触发else
print '*' * 20, "else", '*' * 20
for i in range(10):
    if i < 5:
        continue
    print i
else:
    print "else"

print '*' * 20, "else2", '*' * 20
for i in range(10):
    print i
    if i > 5:
        break
else:
    print "else"

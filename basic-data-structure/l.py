#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "all operations of a list:"
#append, count, extend, index, insert, pop, remove, reverse, sort
print ", ".join([e for e in dir(list) if not e.startswith('_')])

l = []  # define a empty list
print type(l), l  # <type 'list'> []

l = range(10)
print l  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print "there is %d elements in l" % len(l)

# 切片, 和字符串一样
print l[1:2]  # [1]
print l[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 遍历
for e in l:
    print e

print l.count(0)  # 1
print l.index(0)  # 0
# print l.index(100) #Error

#==================== 排序 ====================
l.reverse()  # 反过来, 效果相当于l=l[::-1]
print l  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

l.sort()  # 从小到大排序
print l  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l.sort(reverse=True)  # 倒排, 从大到小
print l  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

l.sort(cmp=lambda x, y: x-y)  # 这个应该是默认
print l  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l.sort(cmp=lambda x, y: y-x)  # 相当于l.sort(reverse=True)
print l  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


#==================== 添加删除修改 ====================
l = range(5)
l.append(100)
print l  # [0, 1, 2, 3, 4, 100]

l.extend([40, 50])
print l  # [0, 1, 2, 3, 4, 100, 40, 50]
l.insert(0, 3.14)
print l  # [3.14, 0, 1, 2, 3, 4, 100, 40, 50]
l.insert(2, "second")  # [3.14, 0, 'second', 1, 2, 3, 4, 100, 40, 50]
print l

l = [1, 1, 1, 2, 2, 3]
l.remove(2)  # 只删除第一个
print l  # [1, 1, 1, 2, 3]
# l.remove(10) #Error
p = l.pop()  # 删除并返回最后一个
print p  # 3
print l  # [1, 1, 1, 2]

l[-1] = 100
print l  # [1, 1, 1, 100]

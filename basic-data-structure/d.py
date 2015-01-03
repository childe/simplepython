#!/usr/bin/env python
# -*- coding: utf-8 -*-

p = {
    "department": {
        "organization_id": 43,
        "alias": "\u673a\u7968",
        "name": "FLT"
    },
    "productline": {
        "organization_id": 43,
        "alias": "\u673a\u7968",
        "name": "FLT"
    },
    "pool": {
        "pool_type": "0",
        "id": 350,
        "name": "gds.engine.flight"
    },
    "servers": [
        {
            "ip": "10.8.89.60",
            "hostname": "VMS01860",
            "idc": "SHAJQ"
            },
        {
            "ip": "10.8.89.59",
            "hostname": "VMS01859",
            "idc": "SHAJQ"
            },
        {
            "ip": "10.8.89.58",
            "hostname": "VMS01858",
            "idc": "SHAJQ"
            }
    ]
}

print type(p), len(p)  # <type 'dict'> 4

print "==================== 字典是无序的 ==================="
print {1: 1, 2: 4} == {2: 4, 1: 1}  # True

print "==================== 取值 ==================="
print p["department"]["name"]  # FLC
# print p["notExistedKey"] #Error
print p.get("notExistedKey")  # None
print p.get("notExistedKey", "~~~")  # ~~~

print "==================== 遍历 ==================="
for k in p:  # 相当于 for k in p.keys():
    print k, ":", p[k]

# 或者是一次取出key和value
print
for k, v in p.items():
    print k, ":", v


print "==================== 赋值 ==================="
d = {}
d["name"] = "square"
d[1] = 1
d[2] = 4
# 打印出来的顺序和赋值的顺序不一样, 是无序的
print d  # {1: 1, 2: 4, 'name': 'square'}

# 后来的赋值会覆盖之前的
d["name"] = "newname"
print d  # {1: 1, 2: 4, 'name': 'newname'}


print "==================== 删除 ==================="
del d["name"]
print d  # {1: 1, 2: 4}
d["name"] = "square"  # 恢复成原来的名字


print "==================== list operations of a dict: ==================="
"""clear, copy, fromkeys, get, has_key, items, iteritems, iterkeys,
itervalues, keys, pop, popitem, setdefault, update, values, viewitems,
viewkeys, viewvalues """
print ", ".join([e for e in dir(dict) if not e.startswith('_')])

print d.keys()  # [1, 2, 'name']
print d.values()  # [1, 4, 'newname']
print d.items()  # [(1, 1), (2, 4), ('name', 'newname')]


print "==================== in ==================="
print 1 in d  # True
print 1 in d  # True

print d.pop(2)  # 4
print d  # {1: 1, 'name': 'square'}
print d.popitem()  # (1, 1) arbitrary, not random
print d  # {'name': 'square'}

# update
d.update({3: 9, 4: 16})
print d  # {3: 9, 4: 16, 'name': 'square'}

print "==================== setdefault ==================="
d.setdefault("name", "new name")
print d["name"]  # square

d.setdefault("alist", [])
print d["alist"]  # []

print "==================== clear ==================="
d.clear()
print d  # {}

print "==================== fromkeys ==================="
print dict.fromkeys([1, 2, 3, 4])  # {1: None, 2: None, 3: None, 4: None}
print dict.fromkeys([1, 2, 3, 4], "0")  # {1: '0', 2: '0', 3: '0', 4: '0'}

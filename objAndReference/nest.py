#!/usr/bin/env python
# -*- coding: utf-8 -*-

pool = {
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

# 这里并没有生成新的对象!
# 只是把department指向了pool["department"]这个已经存在的东西.
department = pool["department"]

department["organization_id"] = 44

print pool  # department.organization_id变化了

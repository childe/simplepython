#!/usr/bin/env python
# -*- coding: utf-8 -*-


def info_supplement(pool):
    if len(pool['servers']) >= 20:
        pool['big'] = True
    else:
        pool['big'] = False

def testfunc(n):
    n = 2
    print n

def test_num():
    n = 10
    testfunc(n)
    print n

def test_obj():
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
    info_supplement(pool)

if __name__ == '__main__':
    test_num()

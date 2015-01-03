#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time


def print_time(func):
    def inner():
        print "start porcess data", time.time()
        func()
        print "porcess data done!", time.time()
    return inner


@print_time
def process_data():
    """定义一个函数,模拟处理数据,需要耗时3-5秒."""
    time.sleep(random.randint(3, 5))


process_data()
process_data()
process_data()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

last_update_time = None


def print_time(func):
    def inner(*args, **kargs):
        print "start porcess data", time.time()
        func(*args, **kargs)
        print "porcess data done!", time.time()
    return inner


def update_data():
    global last_update_time
    print "data expired; update it"
    last_update_time = time.time()


def use_cache(expire_time=30*60):
    def wrapper(func):
        if last_update_time is None or time.time() - last_update_time > expire_time:
            update_data()

        def inner(*args, **kargs):
            func(*args, **kargs)
        return inner
    return wrapper


@use_cache(5*60)
@print_time
def process_data(*args, **kargs):
    """定义一个函数,模拟处理数据,需要耗时3-5秒."""
    time.sleep(random.randint(3, 5))


process_data()
process_data()
process_data()

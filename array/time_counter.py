#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 
  @Author  : chengxin
  @File    : time_counter.py
  @Software: PyCharm
  @Contact : 1031329190@qq.com
  @Desc    : 
"""
import time,timeit

from functools import wraps
import time

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 
  @Author  : chengxin
  @File    : line_search.py
  @Software: PyCharm
  @Contact : 1031329190@qq.com
  @Desc    : 
"""
def line_search(nums,key):
    for i,num in enumerate(nums):
        if num==key:
            return i
    return None
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-03-06
  @Author  : Kaka
  @File    : counting_sort.py
  @Software: PyCharm
  @Contact : 
  @Desc    : 计数排序
"""


def countingSort(nums):
    '''计数排序'''
    k = max(nums) + 1
    numsk = [0] * k
    for num in nums:
        numsk[num] += 1
    numsn = []
    for i,num in enumerate(numsk):
        numsn.extend([i]*num)
    return numsn



if __name__ == '__main__':
    nums = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    countingSort(nums)

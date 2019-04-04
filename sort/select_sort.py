#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-02-19
  @Author  : Kaka
  @File    : select_sort.py
  @Software: PyCharm
  @Contact : 
  @Desc    : 选择排序
"""

def select_sort(nums):
    '''选择排序：'''
    if nums==None or len(nums)<=1:
        return nums
    for i in range(len(nums)):
        min_index=i
        # print("i:%s" % i)
        for j in range(i+1,len(nums)):
            if nums[j]<nums[min_index]:
                min_index = j
        if min_index!=i:
            nums[i],nums[min_index] = nums[min_index],nums[i]
        print("i:%s\t min:%s\t nums:%s" % (i,min_index,nums,))

if __name__ == '__main__':
    nums = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
    select_sort(nums)

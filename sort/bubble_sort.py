#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-02-18
  @Author  : Kaka
  @File    : bubble_sort.py
  @Software: PyCharm
  @Contact : 
  @Desc    : 
"""
def bubble_sort(nums):
    '''冒泡排序'''
    if len(nums)<=1 or nums==None:
        return nums
    # i代表遍历的轮数：每遍历一轮就可以找到一个最大/小值、
    for i in range(len(nums)):
        # 需要比较的数据域随i的增大而减小。len(nums)-i表示要比较的数据 -1是保证下面的j+1不越界
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

if __name__ == '__main__':
    nums = [6,3,4,2,1,5,7]
    bubble_sort(nums)
    print(nums)
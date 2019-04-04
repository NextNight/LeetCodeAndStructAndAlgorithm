#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 
  @Author  : chengxin
  @File    : 
  @Software: PyCharm
  @Contact :
  @Desc    : 
"""
def binary_search(nums, start, end, key):
    """递归实现"""
    if start > end:
        return -1
    # mid = start + int((end-start) / 2)
    mid = (start+end)//2
    if nums[mid] > key:
        return binary_search(nums, start, mid - 1, key)
    elif nums[mid] < key:
        return binary_search(nums, mid + 1, end, key)
    else:
        return mid

def binary_search2(nums, start, end, key):
    """非递归实现"""
    while start <= end:
        mid = (start+end)// 2
        if nums[mid] > key:
            end = mid - 1
        elif nums[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    print(binary_search2(nums,0,len(nums),4))

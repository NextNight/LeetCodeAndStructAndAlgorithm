#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-08
  @Author  : Kaka
  @File    : merge_sort.py
  @Software: PyCharm
  @Contact : 
  @Desc    : 归并排序：分治法，先划分，再排序，再合并。

    递归状态转移方程：
        merger_sort(nums) = merge(merge_sort(nums[:mid]),merge_sort(nums[mid:]))
    终止条件：
        if len(nums)<=1:不再继续分解

    merger_sort:表示排序
    merge      :表示合并


"""
import time

def meger(left, right):
    rs = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            rs.append(left[i])
            i += 1
        else:
            rs.append(right[j])
            j += 1
    if i < len(left):
        rs.extend(left[i:])  # rs+=left[i:]
    if j < len(right):
        rs.extend(right[j:])  # rs+=right[i:]
    return rs


def merge_sort(nums):
    '''递归：'''
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    # 分割
    left, right = nums[:mid], nums[mid:]
    # 排序
    left = merge_sort(left)
    right = merge_sort(right)
    # 合并
    return meger(left, right)


def merge_sort_2(nums):
    '''非递归'''
    nums = [[num] for num in nums ]
    while len(nums)>1:
        ns = []
        for i in range(round(len(nums)/2)):
            ns.append(meger(nums[i*2],nums[i*2+1] if i*2+1<=len(nums)-1 else []))
        nums = ns
    return nums[0]

if __name__ == '__main__':
    test = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print("original:", test)
    start = time.time()
    print("======time start:%s======" % start)
    print("Sorted:", merge_sort(test))
    end = time.time()
    print("======time start:%s======" % (end-start))
    print("Sorted:", merge_sort_2(test))
    end1 = time.time()
    print("======time start:%s======" % (end1-end))
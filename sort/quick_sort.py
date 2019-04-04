#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-03-08
  @Author  : Kaka
  @File    : quick_sort.py
  @Software: PyCharm
  @Contact : 
  @Desc    : 快速排序：分治法不断将数据分割为带基准数据和小于基准数据两部分

"""

def quick_sort(nums):
    '''快速排序：递归'''
    if len(nums)<=1:return nums
    left,right=[],[]
    midt = nums[len(nums)//2]
    nums.remove(midt)
    for num in nums:
        if num>=midt:
            right.append(num)
        else:
            left.append(num)
    return quick_sort(left)+[midt]+quick_sort(right)

def quick_sort_2(nums,left,right):
    '''TODO：未完成'''
    if len(nums)<=1:return nums
    i,j,midt =0,len(nums)-1,nums[0]
    while i<=j:
        #凑头往左遍历知道第一个小于midt停下
        while nums[j]>midt:
                j-=1
        nums[i] = nums[j]
        while nums[i]<midt:
                nums[j]=nums[i]
                i+=1
    nums[i]=midt
    return


if __name__ == '__main__':
    nums = [2,4,1,5,2,6,7,2,9,3]
    print(quick_sort_2(nums))

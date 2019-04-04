#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 
  @Author  : chengxin
  @File    : moveZeroes.py
  @Software: PyCharm
  @Contact : 1031329190@qq.com
  @Desc    :
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    示例:
        输入: [0,1,0,3,12]
        输出: [1,3,12,0,0]
    说明:
    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。
"""

def moveZeroes(nums):
    if nums == None or len(nums) == 1:
        return
    k = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[k] = nums[i]
            k += 1
        print("%d:%s" % (k, nums))
    while k < len(nums):
        nums[k] = 0
        k += 1
        print("%d:%s" % (k, nums))
    return nums

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)

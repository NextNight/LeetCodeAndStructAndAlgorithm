#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-02-21
  @Author  : Kaka
  @File    : mergeTowArray.py
  @Software: PyCharm
  @Contact : 
  @Desc    :https://leetcode-cn.com/problems/merge-sorted-array/
  给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
    说明:
        初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
        你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    示例:
        输入:
            nums1 = [1,2,3,0,0,0], m = 3
            nums2 = [2,5,6],       n = 3
        输出: [1,2,2,3,5,6]
"""


def merge(nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if nums1 == None or m == 0:
        for i, num in enumerate(nums2):
            nums1[i] = num
        return
    index = m + n - 1
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[index] = nums1[m - 1]
            m -= 1
        else:
            nums1[index] = nums2[n - 1]
            n -= 1
        index -= 1
    while n > 0:
        nums1[index] = nums2[n - 1]
        n -= 1
        index -= 1


if __name__ == '__main__':
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(nums1)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-04
  @Author  : Kaka
  @File    : threeSum.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/3sum/
  @Desc    : 三数之和
"""

class Solution(object):
    def threeSum(self, nums):
        """TODO：未完成
        :type nums: List[int]
        :rtype: List[List[int]]
        a+b+c==0 => a+b==-c 必定存在负数，
        """
        nums = sorted(nums)
        l = len(nums)
        for i in range(l-3):
            p,e = i,l-i-1






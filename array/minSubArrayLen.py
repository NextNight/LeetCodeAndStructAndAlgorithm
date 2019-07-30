#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-07-29
  @Author  : Kaka
  @File    : minSubArrayLen.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/minimum-size-subarray-sum/
  @Desc    : 长度最小子数组
  给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""


class Solution:
    def minSubArrayLen(self, s, nums):
        '''双指针+滑窗'''
        p, r, w = 0, 0, len(nums)
        while r <= len(nums) - 1:
            if sum(nums[p:r + 1]) >= s:
                w = min(r - p + 1, w)
                p += 1
            else:
                r += 1
        if w == len(nums) and sum(nums) < s:
            return 0
        return w

    def minSubArrayLen_(self, s, nums):
        '''双指针+滑窗:优化版'''
        p, r, w = 0, 0, len(nums)
        while r <= len(nums) - 1:
            if sum(nums[p:r + 1]) >= s:
                w = r - p + 1
                p += 1
            else:
                if r - p + 1 < w:
                    r += 1
                else:
                    p += 1
        if w == len(nums) and sum(nums) < s:
            return 0
        return w


if __name__ == '__main__':
    solu = Solution()
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(solu.minSubArrayLen(s, nums))

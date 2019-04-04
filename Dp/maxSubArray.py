#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-02-21
  @Author  : Kaka
  @File    : maxSubArray.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/maximum-subarray/
  @Desc    :
  给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    示例:
        输入: [-2,1,-3,4,-1,2,1,-5,4],
        输出: 6
        解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


class Solution:
    def maxSubArray(self, nums: 'List[int]'):
        if len(nums) == 0 or nums == None:
            return None
        sum_all = nums[0]
        sum_cur = 0
        for num in nums:
            sum_cur += num
            if sum_cur > sum_all:
                sum_all = sum_cur
            if sum_cur < 0:
                sum_cur = 0
        return sum_all

    def maxSubArray2(self, nums):
        if len(nums) == 0 or nums == None:
            return None
        sum_all = nums[0]
        sum_cur = 0
        for num in nums:
            sum_cur += num
            sum_all = max(sum_all, sum_cur)
            sum_cur = 0 if sum_cur < 0 else sum_cur
        return sum_all

    def maxSubArray3(self, nums):
        if len(nums) == 0 or nums == None:
            return None
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solu =Solution()
    print(solu.maxSubArray3(nums))

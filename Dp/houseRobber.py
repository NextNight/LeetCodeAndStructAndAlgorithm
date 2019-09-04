#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-02-26
  @Author  : Kaka
  @File    : houseRobber.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/house-robber/
  @Desc    : 打家劫舍
  你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

    示例 1:

        输入: [1,2,3,1]
        输出: 4
        解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
             偷窃到的最高金额 = 1 + 3 = 4 。
    示例 2:

        输入: [2,7,9,3,1]
        输出: 12
        解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
             偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""


class Solution:
    def rob(self, nums: 'List[int]') -> int:
        '''打家劫舍'''
        if any([nums == None, len(nums) == 0]): return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        return max(nums[len(nums) - 1] + self.rob(nums[:len(nums) - 2]),self.rob(nums[:len(nums) - 1]))

    def rob_2(self, nums: 'List[int]') -> int:
        '''打家劫舍'''
        if any([nums == None, len(nums) == 0]): return 0
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        max_p = [0] * (n)
        max_p[n - 1] = max(nums[n - 1] + self.rob(nums[:n - 2]),self.rob(nums[:n - 1]))
        return max_p[n - 1]

    def rob_3(self, nums: 'List[int]') -> int:
        '''打家劫舍'''
        if any([nums == None, len(nums) == 0]): return 0
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        max_p = [0] * n
        if max_p[n - 1] == 0:
            max_p[n - 1] = max(nums[n - 1] + self.rob(nums[:n - 2]),self.rob(nums[:n - 1]))
        else:
            return max_p[n - 1]
        return max_p[n - 1]

    def rob_4(self, nums: 'List[int]') -> int:
        '''打家劫舍:DP'''
        if any([nums == None, len(nums) == 0]): return 0
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        max_p = [0] * n
        max_p[0],max_p[1] = nums[0],max(nums[0], nums[1])
        for i in range(2, len(nums)):
            max_p[i] = max(max_p[i-1],max_p[i-2]+nums[i])
        return max_p[n - 1]


if __name__ == '__main__':
    solu = Solution()
    nums = [2, 7, 9, 3, 1, 2]
    print(solu.rob_4(nums))

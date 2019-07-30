#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-07-29
  @Author  : Kaka
  @File    : findMaxConsecutiveOnes.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/max-consecutive-ones/
  @Desc    :最大连续1的个数
  给定一个二进制数组， 计算其中最大连续1的个数。

    示例 1:

    输入: [1,1,0,1,1,1]
    输出: 3
    解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
    注意：

    输入的数组只包含 0 和1。
    输入数组的长度是正整数，且不超过 10,000。
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        '''转字符串切割
        '''
        if nums is None:
            return nums
        return max(list(map(lambda x: len(x), ''.join(list(map(lambda x: str(x), nums))).split('0'))))

if __name__ == '__main__':
    solu =Solution()
    nums = []#[1,1,0,1,1,1]
    print(solu.findMaxConsecutiveOnes(nums))
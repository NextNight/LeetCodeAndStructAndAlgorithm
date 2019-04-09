#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-09
  @Author  : Kaka
  @File    : searchMidIndex.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/find-pivot-index/
  @Desc    : 寻找数组的中心索引

  给定一个整数类型的数组  nums，请编写一个能够返回数组“中心索引”的方法。

    的英文我们定义这样数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

    如果数组不存在中心索引，那么我们应该返回-1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

    示例1：

    输入：
    nums = [1,7,3,6,5,6]
    输出： 3
     解释：
    索引3（nums [3] = 6）的左侧数之和（1 + 7 + 3 = 11），与右侧数之和（5 + 6 = 11）相等。
    同时，3也是第一个符合要求的中心索引。
    示例2：

    输入：
    nums = [1,2,3]
    输出： -1
     解释：
    数组中不存在满足此条件的中心索引。
    说明：

    nums的长度范围为  [0, 10000]。
    一个任何  nums[i]将会的英文一个范围在  [-1000, 1000]的整数。
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return -1
        sums = sum(nums)
        s = 0
        for i, num in enumerate(nums):
            if sums-s-num == s:
                return i
            else:
                s += num
        return -1


if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    solu = Solution()
    print("index:%s" % solu.pivotIndex(nums))

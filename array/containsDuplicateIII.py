#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-07
  @Author  : Kaka
  @File    : containsDuplicateIII.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/contains-duplicate-iii/
  @Desc    : 存在重复元素III
  给定一个整数数组，判断数组中是否有两个不同的索引i和j，使得  nums [i]和  nums [j]  的差的绝对值最大为t，并且i和j之间的差的绝对值最大为ķ。

    示例1：

    输入： nums = [1,2,3,1]，k  = 3，t = 0
     输出： true
    示例2：

    输入： nums = [1,0,1,1]，k  =  1，t = 2
     输出： true
    示例3：

    输入： nums = [1,5,9,1,5,9]，k = 2，t = 3
     输出： false
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """TODO:10000超时
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        leng = len(nums)
        if leng <= 1: return False
        # 后置窗口
        # ===========version.1=========
        # for i,num in enumerate(nums[:-1]):
        #     for j in range(i+1,min(i+k+1,leng)):
        #         if abs(nums[j]-nums[i])<=t:
        #             return True
        # return False

        # ===========version.2=========
        # for i,num in enumerate(nums[:-1]):
        #     win = set(nums[i+1:min(i+k+1,leng)])
        #     for mun in win:
        #         if abs(mun-num)<=t:
        #             return True
        # return False

        # 前置窗口：set使用很巧妙
        # ===========version.3=========
        win = set()
        for i, num in enumerate(nums):
            if t == 0:
                if num in win:
                    return True
            else:
                for w in win:
                    if abs(num - w) <= t:
                        return True
            win.add(num)
            if len(win) > k:
                win.remove(nums[i - k])
        return False


if __name__ == '__main__':
    # nums ,k,t= [1,5,9,1,5,9],2,3
    nums, k, t = [1, 0, 1, 1], 1, 2
    solu = Solution()
    print(solu.containsNearbyAlmostDuplicate(nums, k, t))

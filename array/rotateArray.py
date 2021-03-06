#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-07-29
  @Author  : Kaka
  @File    : rotate.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/rotate-array/
  @Desc    : 旋转数组
  给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

    示例 1:

    输入: [1,2,3,4,5,6,7] 和 k = 3
    输出: [5,6,7,1,2,3,4]
    解释:
    向右旋转 1 步: [7,1,2,3,4,5,6]
    向右旋转 2 步: [6,7,1,2,3,4,5]
    向右旋转 3 步: [5,6,7,1,2,3,4]
    示例 2:

    输入: [-1,-100,3,99] 和 k = 2
    输出: [3,99,-1,-100]
    解释:
    向右旋转 1 步: [99,-1,-100,3]
    向右旋转 2 步: [3,99,-1,-100]
    说明:

    尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    要求使用空间复杂度为 O(1) 的 原地 算法。
"""


class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        方案：向右移动k等于把末尾k个元素放到开头
        """
        if len(nums) == 1 or nums is None:
            return
        if k >= len(nums):
            k = k - len(nums)
        if k < len(nums) / 2:  # 右移
            sub = nums[-k:]
            print(sub)
            for i in range(len(nums) - 1, k - 1, -1):
                nums[i] = nums[i - k]
            for i in range(k):
                nums[i] = sub[i]
        else:  # 左移
            k = len(nums) - k
            sub = nums[:k]
            for i in range(len(nums) - k):
                nums[i] = nums[i + k]
            for i in range(-k, 0, 1):
                nums[i] = sub[i]

    def rotate_(self, nums, k) -> None:
        '''三步翻转法：但是不是原地算法需要返回值'''
        if len(nums) == 1 or nums is None:
            return
        nums = nums[:-k][::-1] + nums[-k:][::-1]
        nums = nums[::-1]
        print(nums)


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solu.rotate_(nums, k)
    print(nums)

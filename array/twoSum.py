#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-07-29
  @Author  : Kaka
  @File    : twoSum.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
  @Desc    :两数之和 II - 输入有序数组
  给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

    函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

    说明:

    返回的下标值（index1 和 index2）不是从零开始的。
    你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
    示例:

    输入: numbers = [2, 7, 11, 15], target = 9
    输出: [1,2]
    解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""


class Solution:
    def twoSum(self, numbers, target):
        '''字典边存边查看是否满足'''
        num_dic = {}
        for i, num in enumerate(numbers):
            if num_dic.get(target - num) is not None:
                return [num_dic.get(target - num) + 1, i + 1]
            else:
                num_dic[num] = i

        return [-1,-1]

    def twoSum_(self, numbers, target):
        '''双指针法：有效利用有序数组这个条件
        '''
        left, right = 0, len(numbers) - 1
        while left < right:
            sums = numbers[left] + numbers[right]
            if sums > target:
                right -= 1
            elif sums < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return [-1, -1]


if __name__ == '__main__':
    solu = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(solu.twoSum_(numbers, target))

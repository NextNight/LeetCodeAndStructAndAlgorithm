#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-02
  @Author  : Kaka
  @File    : arrayIntersectI.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/intersection-of-two-arrays
  @Desc    : 两个数组的交集I

  给定两个数组，编写一个函数来计算它们的交集。

    示例 1:

        输入: nums1 = [1,2,2,1], nums2 = [2,2]
        输出: [2]
        示例 2:

        输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        输出: [9,4]
        说明:

        输出结果中的每个元素一定是唯一的。
        我们可以不考虑输出结果的顺序。
"""
class Solution:
    @staticmethod
    def intersection( nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        return list(set(nums1) & set(nums2))

    @staticmethod
    def intersect2(nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        """使用hash"""
        dic ={}
        for num in nums1:
            if dic.get(num)==None:
                dic[num]=1
            else:
                dic[num]+=1
        for num in nums2:
            if dic.get(num) == None:
                dic[num] = 1
            else:
                dic[num] += 1
        inners = []
        for key in dic:
            if dic[key]>1:
                inners.append(key)
        return inners

if __name__ == '__main__':
    nums1, nums2 = [4, 9, 5, 9, 4], [9, 4, 9, 8, 4]
    print(Solution.intersect2(nums1=nums1, nums2=nums2))

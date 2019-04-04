#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-02
  @Author  : Kaka
  @File    : arrayIntersect.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
  @Desc    : 两个数组交集II
  给定两个数组，编写一个函数来计算它们的交集。
    示例 1:

    输入: nums1 = [1,2,2,1], nums2 = [2,2]
    输出: [2,2]
    示例 2:

    输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出: [4,9]
    说明：

    输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
    我们可以不考虑输出结果的顺序。
    进阶:

    如果给定的数组已经排好序呢？你将如何优化你的算法？
    如果 nums1 的大小比 nums2 小很多，哪种方法更优？
    如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

"""


class Solution:
    @staticmethod
    def intersect(nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        '''使用set'''
        inner = set(nums1) & set(nums2)
        inners = []
        for num in inner:
            inners.append([num] * min(nums1.count(num), nums2.count(num)))
        return inners

    @staticmethod
    def intersect2(nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        """使用两个dict"""
        d1, d2 = {}, {}
        for num in nums1:
            if d1.get(num) == None:
                d1[num] = 1
            else:
                d1[num] += 1
        for num in nums2:
            if d2.get(num) == None:
                d2[num] = 1
            else:
                d2[num] += 1
        inners = []
        for key in d1 if len(d1) < len(d2) else d2:
            if d1.get(key) != None and d2.get(key) != None:
                inners.extend([key] * min(d1.get(key), d2.get(key)))
        return inners

    @staticmethod
    def intersect3(nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        '''使用一个dict'''
        inners,dic = [],{}
        for num in nums1:
            if dic.get(num) == None:
                dic[num] = 1
            else:
                dic[num] += 1

        for num in nums2:
            if dic.get(num)!=None and  dic[num]>0:
                inners.append(num)
                dic[num]-=1
        return inners




if __name__ == '__main__':
    nums1, nums2 = [4, 5, 9, 4], [9, 4, 9, 8, 4]
    print(Solution.intersect3(nums1=nums1, nums2=nums2))

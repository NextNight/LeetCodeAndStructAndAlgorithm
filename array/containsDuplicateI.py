#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-02
  @Author  : Kaka
  @File    : containsDuplicate.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/contains-duplicate/
  @Desc    : 存在重复元素I
  给定一个整数数组，判断是否存在重复元素。

    如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

    示例 1:

    输入: [1,2,3,1]
    输出: true
    示例 2:

    输入: [1,2,3,4]
    输出: false
    示例 3:

    输入: [1,1,1,3,3,4,3,2,4,2]
    输出: true
"""


class Solution:
    @staticmethod
    def containsDuplicate(nums: 'List[int]') -> bool:
        dic = {}
        for num in nums:
            if dic.get(num)!=None:
                return True
            else:
                dic[num]=num
        return False

    @staticmethod
    def containsDuplicate2(nums: 'List[int]') -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
               s.add(num)
        return False

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-02
  @Author  : Kaka
  @File    : containsDuplicateII.py.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/contains-duplicate-ii/
  @Desc    : 存在重复元素II
  给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

    示例 1:

    输入: nums = [1,2,3,1], k = 3
    输出: true
    示例 2:

    输入: nums = [1,0,1,1], k = 1
    输出: true
    示例 3:

    输入: nums = [1,2,3,1,2,3], k = 2
    输出: false
"""


class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: int) -> bool:
        '''dict,O(n),O(n)'''
        dic ={}
        for i,num in enumerate(nums):
            if dic.get(num)==None:
                dic[num] =[i]
            else:
                dic[num].append(i)

        for key in dic:
            if len(dic[key])>=2:
                for j,id in enumerate(dic[key][:-1]):
                    if abs(dic[key][j]-dic[key][j+1])<=k:
                        return True
        return False

    def containsNearbyDuplicate2(self, nums: 'List[int]', k: int) -> bool:
        '''优化：不必存储一个数所有出现的索引列表，只需要用后一个索引-前一个索引看是否满足条件'''
        dic ={}
        for i,num in enumerate(nums):
            if dic.get(num)==None:
                dic[num] =i
            elif i-dic[num]<=k:
                return True
            else:
                dic[num] = i
        return False

if __name__ == '__main__':
    solu = Solution()
    nums,k=[1,2,3,1,2,3],2
    # nums,k=[1,0,1,1],1
    print(solu.containsNearbyDuplicate2(nums,k))



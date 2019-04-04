#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-03-04
  @Author  : Kaka
  @File    : majorityElement.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/majority-element/comments/
  @Desc    : 求众数
  给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

    你可以假设数组是非空的，并且给定的数组总是存在众数。

    示例 1:

    输入: [3,2,3]
    输出: 3
    示例 2:

    输入: [2,2,1,1,1,2,2]
    输出: 2
"""


class Solution:
    def majorityElement(self, nums: 'List[int]') -> int:
        '''摩尔投票法:O(n),O(1)'''
        maj,count = 0,0
        for item in nums:
            if count==0:
                maj=item
            if item==maj:
                count+=1
            else:
                count-=1
        return maj

    def majorityElement_2(self, nums: 'List[int]') -> int:
        '''哈希存储:O(n),O(n)'''
        numc = {}
        for num in nums:
            if numc.get(num)==None:
                numc[num]=1
            else:
                numc[num]+=1
        # maxk, maxv = 0, 0
        # for item in numc.items():
        #     if item[1] > maxv:
        #         maxk, maxv = item[0], item[1]
        # return maxk
        for item in numc.items():
            if item[1]>len(nums)/2:
                 return item[0]

    def majorityElement_3(self, nums: 'List[int]') -> int:
        '''哈希存储:O(n),O(n)+sort'''
        numc = {}
        for num in nums:
            if numc.get(num) == None:
                numc[num] = 1
            else:
                numc[num] += 1
        return sorted(numc.items(),key=lambda x:x[1]).pop()[0]

    def majorityElement_4(self, nums: 'List[int]') -> int:
        '''最牛解法'''
        return sorted(nums)[len(nums)//2]

if __name__ == '__main__':
    solu =Solution()
    nums =[3,3,4,4,4,5,5,5,6,6,]
    print(solu.majorityElement_4(nums))





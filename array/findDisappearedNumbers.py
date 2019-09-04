#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-29
  @Author  : Kaka
  @File    : findDisappearedNumbers.py
  @Software: PyCharm
  @Contact : 
  @Desc    : 找到所有数组中消失的数字
  给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
    找到所有在 [1, n] 范围之间没有出现在数组中的数字。

    您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

    示例:

    输入:
    [4,3,2,7,8,2,3,1]

    输出:
    [5,6]

"""

class Solution:
    def findDisappearedNumbers(self, nums):
        '''
        方案：∵ n是数组大小同时也是最大的数，如果不存在消失的数，那么1-n个数一定会都出现一次，那么就对应0-n-1号位每个位置一个数，
             ∴ 遍历数组，对于a[i]这个数，他应该对应下标为a[i],那么给a[a[i]]+n,得到新的数组
             ∵ 如果数字i没有出现过，那么第i-1号下标的数就不会+n,索引遍历新数组如果a[i]<n，那么
        '''
        rs = []
        for num in nums:
            if num > 2*len(nums):
                num = num-2*len(nums)
            elif num > len(nums):
                num = num - len(nums)
            nums[num-1]+=len(nums)
        for i,num in enumerate(nums):
            if num <=len(nums):
                rs.append(i+1)
        return rs

if __name__ == '__main__':
    solu = Solution()
    nums= [4,3,2,7,7,2,3,1]
    solu.findDisappearedNumbers(nums)
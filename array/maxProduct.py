#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-03-06
  @Author  : Kaka
  @File    : maxProduct.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/maximum-product-subarray/
  @Desc    : 乘积最大子序列
  给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

    示例 1:

    输入: [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 有最大乘积 6。
    示例 2:

    输入: [-2,0,-1]
    输出: 0
    解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""


class Solution:
    def maxProduct(self, A):
        '''TODO:先计算从左到右的相乘的最大值，再计算从右到左的最大值；再将两组最大值相比'''
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)

    def maxProduct2(self, A):
        '''动态规划
        整个乘积最大序列分三种情况：
            第n个数有三种情况：正数，负数，0，
            当前n-1个数是：正数，正数*正数最大，负数，负数*负数最大，0，正数最大
            所以最大只有三种情况：
                1. 前n - 1位的乘积最小子序列的乘积 * A[n]最大
                2. 前n - 1位的乘积最大子序列的乘积 * A[n]最大
                3. 前n - 1位的乘积最大子序列和乘积最小子序列的乘积 * A[n]都不是最大，而A[n]本身最大。
        max(d[n]) = max(max(d[n-1]*d[n],min(d[n-1]),d[n]))
        min(d[n]) = min(max(d[n-1]*d[n],min(d[n-1]),d[n]))
        '''
        if len(A) < 1: return None
        max_dn, min_dn = 1, 1
        max_rs = A[0]
        for a in A:
            ma = max_dn
            max_dn = max(ma * a, min_dn * a, a)
            min_dn = min(ma * a, min_dn * a, a)
            max_rs = max(max_dn, max_rs)
        return max_rs


if __name__ == '__main__':
    nums = [-4, -3, -2]
    # nums = [2,0,3,-2,4,0,3]
    solu = Solution()
    print(solu.maxProduct2(nums))

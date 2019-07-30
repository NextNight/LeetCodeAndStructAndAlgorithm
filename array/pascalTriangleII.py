#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-07-30
  @Author  : Kaka
  @File    : pascalTriangleII.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/pascals-triangle-ii/
  @Desc    :杨辉三角 II
  给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

    在杨辉三角中，每个数是它左上方和右上方的数的和。

    示例:

    输入: 3
    输出: [1,3,3,1]
    进阶：

    你可以优化你的算法到 O(k) 空间复杂度吗？
"""


class Solution:
    def getRow_(self,rowIndex):
        '''使用两个数组A，B'''
        if  rowIndex==0:return [1]
        A = [1]
        B = [1]*(rowIndex+1)
        for i in range(1,rowIndex+1):
            for j in range(i+1):
                if j ==0:
                    B[j] = A[j]
                elif j==i:
                    B[j]=A[j-1]+0
                else:
                    B[j] = A[j-1]+A[j]
            A = B[:i+1]
        return A

if __name__ == '__main__':
    solu = Solution()
    solu.getRow_(3)
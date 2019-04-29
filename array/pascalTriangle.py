#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-28
  @Author  : Kaka
  @File    : pascalTriangle.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/pascals-triangle/
  @Desc    : 杨辉三角
  给定一个非负整数  numRows行，生成杨辉三角的前  numRows行 行。

    在杨辉三角中，每个数是它左上方和右上方的数的和。

    示例：

    输入： 5
     输出：
    [
         [1]，
        [1,1]，
       [1,2,1]
      [1,3,3,1]，
     [1,4,6,4,1]
    ]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        思路：
            i行有i+1个数
            所有行的第一个数为1，第j个数为前一行的第j个数和第j-1个数相加。
        """
        if numRows==1:return [[1]]
        result = []
        for i in range(numRows):
            if i==0:
                result.append([1])
                continue
            s = []
            for j in range(i+1):
                if j ==0:
                    s.append(1)
                    continue
                x= result[i-1][j-1]
                if j>=len(result[i-1]):
                    y = 0
                else:
                    y = result[i-1][j]
                s.append(x+y)
            result.append(s)
        return  result

if __name__ == '__main__':
    solu =Solution()
    solu.generate(5)
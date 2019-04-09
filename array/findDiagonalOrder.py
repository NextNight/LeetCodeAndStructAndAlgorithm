#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-09
  @Author  : Kaka
  @File    : findDiagonalOrder.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/diagonal-traverse/
  @Desc    : 对角线遍历
  给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。


    示例:

    输入:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]

    输出:  [1,2,4,7,5,3,6,8,9]

    解释:

"""


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """TODO:未完成
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        rs = [matrix[i][j]]

        # 向右拐：i-,j+
        # 向下拐：i+,j-
        s = 0
        while True:
            if s == 0:
                i += 1
                rs.append(matrix[i][j])
                while i >= 0:
                    i -= 1
                    j += 1
                    rs.append(matrix[i][j])
                s = 1
            if s == 1:
                j += 1
                rs.append(matrix[i][j])
                while j >= 0:
                    i += 1
                    j -= 1
                    rs.append(matrix[i][j])
                s = 0
            if i == m and j == n:
                break
        print(rs)


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    solu = Solution()
    solu.findDiagonalOrder(matrix)

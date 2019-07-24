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

    解释:  之字形遍历

    方案：
        1、先得到[[1],[2,4],[3,5,7],[6,8],[9]]
        2、遍历，且奇数行翻转得到 [1,2,4,7,5,3,6,8,9]
        回到根本问题：
            如何得到1的结果？，观察发现1中每个数组的开头是顺序的第一行和最后一列，也就是矩阵的一个拐角，这个拐角上每个元素g的意义是什么呢，
            根据每个元素g(x,y)的坐标可遇得到与其在一条对角线的上的所有元素的坐标。只需对元素g的坐标不断做左下平移即(x+1,y-1)操作。操作一次得到一个坐标w，
            退出条件是:w的横坐标wy<=m-1 and 横坐标wx>=0  ,

"""


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] or matrix is None:
            return matrix

        def point_add(a, b):
            return (a[0] + b[0], a[1] + b[1])

        m, n = len(matrix), len(matrix[0])  # m行n列
        titlen = [(0, i) for i in range(n)]
        titlem = [(i, n - 1) for i in range(1, m, 1)]
        title = titlen + titlem
        rs, line = [], []
        for i, item in enumerate(title):
            # 循环条件1
            # max_x = min(m - 1, item[0] + item[1])
            # while item[0] <= max_x:

            # 循环条件2
            while item[0] <= m - 1 and item[1] >= 0:
                line.append(item)
                item = point_add(item, (1, -1))
            if i % 2 == 0:
                line = list(reversed(line))
            rs.extend(line)
            line = []
        rs = [matrix[item[0]][item[1]] for item in rs]
        return rs

    def findDiagonalOrder_(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) <= 0 or matrix is None:
            return matrix
        m, n = len(matrix), len(matrix[0])
        titlen = [(0, i) for i in range(n)]
        titlem = [(i, n - 1) for i in range(1, m, 1)]
        title = titlen + titlem
        print(title)
        rs = []
        for i, item in enumerate(title):
            line = []
            while item[0] <= m - 1 and item[1] >= 0:
                line.append(item)
                item = (item[0] + 1, item[1] - 1)
            if i % 2 == 0:
                line = list(reversed(line))
            rs.extend(line)
        rs = [matrix[item[0]][item[1]] for item in rs]
        return rs


if __name__ == '__main__':
    # matrix = [
    #     [1, 2, 3, 11],
    #     [4, 5, 6, 12],
    #     [7, 8, 9, 13]
    # ]
    matrix = [[3], [2]]
    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9],
    #     [10, 11, 12]
    # ]
    solu = Solution()
    solu.findDiagonalOrder(matrix)

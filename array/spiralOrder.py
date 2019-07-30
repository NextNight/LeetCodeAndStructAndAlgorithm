#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-07-25
  @Author  : Kaka
  @File    : spiralOrder.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/spiral-matrix/
  @Desc    : 螺旋矩阵遍历
  给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

    示例 1:

    输入:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    输出: [1,2,3,6,9,8,7,4,5]
    示例 2:

    输入:
    [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix):
        if matrix == [] or matrix is None:
            return matrix
        m, n = len(matrix), len(matrix[0])
        location = [(0, 0)]

        def left():
            point = location[-1]
            while point[1] > 0:
                point = (point[0], point[1] - 1)
                if not point in location:
                    location.append(point)
                else:
                    return

        def right():
            point = location[-1]
            while point[1] < n - 1:
                point = (point[0], point[1] + 1)
                if not point in location:
                    location.append(point)
                else:
                    return

        def push():
            point = location[-1]
            while point[0] > 0:
                point = (point[0] - 1, point[1])
                if not point in location:
                    location.append(point)
                else:
                    return

        def down():
            point = location[-1]
            while point[0] < m - 1:
                point = (point[0] + 1, point[1])
                if not point in location:
                    location.append(point)
                else:
                    return

        while len(location) < m * n:
            right()
            down()
            left()
            push()

        rs = [matrix[p[0]][p[1]] for p in location]
        return rs


if __name__ == '__main__':
    solu = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    solu.spiralOrder(matrix)

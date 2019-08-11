#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-01
  @Author  : Kaka
  @File    : rotateImage.py
  @Software: PyCharm
  @Contact : 
  @Desc    : 旋转图像
  给定一个 n × n 的二维矩阵表示一个图像。

    将图像顺时针旋转 90 度。

    说明：

    你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

    示例 1:

    给定 matrix =
        [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ],

    原地旋转输入矩阵，使其变为:
        [
          [7,4,1],
          [8,5,2],
          [9,6,3]
        ]
    示例 2:

    给定 matrix =
        [
          [ 5, 1, 9,11],
          [ 2, 4, 8,10],
          [13, 3, 6, 7],
          [15,14,12,16]
        ],

    原地旋转输入矩阵，使其变为:
        [
          [15,13, 2, 5],
          [14, 3, 4, 1],
          [12, 6, 8, 9],
          [16, 7,10,11]
        ]
"""


class Solution:
    def rotate(self, matrix) -> None:
        """
        方案：先上下翻转->载左下右上对角翻转==顺时针90°
        Do not return anything, modify matrix in-place instead.
        """
        # 上下翻转
        n = len(matrix)
        for i in range(n - 1):
            if i >= n - 1 - i:
                break
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
        # 左下右上翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate_(self, matrix) -> None:
        '''🐂牛皮哦'''
        matrix[:] = map(list, zip(*matrix[::-1]))

if __name__ == '__main__':
    solu = Solution()
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    solu.rotate_(matrix)
    assert matrix == [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]

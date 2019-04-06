#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-04
  @Author  : Kaka
  @File    : numberOfBoomerangs.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/number-of-boomerangs/
  @Desc    : 回旋镖的数量

  给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

    找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

    示例:

    输入:
    [[0,0],[1,0],[2,0]]

    输出:
    2

    解释:
    两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]

    =======

    计算一个点到其他点的距离，相同的两个距离构成两个回旋镖，Ac=d,Ad=d,那么Acd，Adc就是两个回旋镖。

    =======
"""


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(p1,p2):
            return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2

        if len(points)<3:return 0
        num = 0
        dic =[]
        for i,pt in enumerate(points[:-2]):
            for j,px in enumerate(points[1:]):
                dis = distance(pt,px)
                if dic.count(dis)>0:
                    pass# num+=dic.count(dis)
                dic.append(dis)






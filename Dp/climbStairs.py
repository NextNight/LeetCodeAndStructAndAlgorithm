#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-02-21
  @Author  : Kaka
  @File    : maxSubArray.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/climbing-stairs/
  @Desc    : 爬楼梯问题：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
                       每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""
import numpy as np


# 递归一定能解决问题，但是数值太大的时候会溢出，或者计算超时
def climbStairs(n):
    """递归"""
    if (n < 0 or n == None): return None
    if (n == 0 or n == 1): return 1
    return climbStairs(n - 1) + climbStairs(n - 2)


def climbStairs2(n):
    """递归：去冗余"""
    if (n < 0 or n == None): return None
    mr = [-1] * (n + 1)
    if (n == 0 or n == 1): return 1
    if mr[n] == -1:
        mr[n] = climbStairs2(n - 1) + climbStairs2(n - 2)
        return mr[n]
    if mr[n] != -1:
        return mr[n]


def climbStairs3(n):
    """递推式"""
    if n == None or n < 0: return None
    if n == 1: return 1
    if n == 2: return 2
    mr = [-1] *(n+1)
    mr[1], mr[2] = 1, 2
    for i in np.arange(3, n + 1):
        mr[i] = mr[i - 1] + mr[i - 2]
    return mr[n]


if __name__ == '__main__':
    print(climbStairs(3))
    print(climbStairs2(3))
    print(climbStairs3(5))

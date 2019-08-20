#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-16
  @Author  : Kaka
  @File    : fibonacciNumber.py
  @Software: PyCharm
  @Contact : 
  @Desc    : 斐波那契数
  斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
    给定 N，计算 F(N)。

     

    示例 1：

    输入：2
    输出：1
    解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
    示例 2：

    输入：3
    输出：2
    解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
    示例 3：

    输入：4
    输出：3
    解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
     

    提示：

    0 ≤ N ≤ 30

"""
lookup = {}

class Solution:
    def fib(self, N):
        '''递归解法'''
        if N <= 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N - 1) + self.fib(N - 2)

    def fib_v2(self, N):
        '''递归+查找表'''
        if N <= 1:
            return N
        if lookup.get(N) != None:
            return lookup[N]
        result = self.fib(N - 1) + self.fib(N - 2)
        lookup[N] = result
        return result

    def fib_v3(self, N):
        '''迭代:O(n) O(n)'''
        rs = [0, 1]
        for i in range(2, N + 1):
            rs.append(rs[i - 1] + rs[i - 2])
        return rs[-1]


if __name__ == '__main__':
    solu = Solution()
    print(solu.fib_v3(30))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-06
  @Author  : Kaka
  @File    : isHappy.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/happy-number/
  @Desc    : 快乐数

    编写一个算法来判断一个数是不是“快乐数”。

    一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

    示例:

    输入: 19
    输出: true
    解释:
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        dic = set()
        while True:
            sum = 0
            while n > 0:
                sum += (n % 10) ** 2
                n //= 10
            if sum in dic:
                return False
            elif sum == 1:
                return True
            else:
                dic.add(sum)

            n = sum

if __name__ == '__main__':
    solu = Solution()
    print(solu.isHappy(1))

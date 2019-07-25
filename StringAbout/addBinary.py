#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-29
  @Author  : Kaka
  @File    : addBinary.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/add-binary/
  @Desc    : 二进制相加
  给定两个二进制字符串，返回他们的和（用二进制表示）。

    输入为非空字符串且只包含数字 1 和 0。

    示例 1:

    输入: a = "11", b = "1"
    输出: "100"
    示例 2:

    输入: a = "1010", b = "1011"
    输出: "10101"
"""


class Solution(object):
    def addBinary(self, a, b):
        '''内置函数
        bin(5):转2进制
        oct(5):转8进制
        hex(5):转16进制
        '''
        return bin(eval('0b' + a) + eval('0b' + b))[2:]

    def addBinary2(self, a, b):
        '''内置函数'''
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary3(self, a, b):
        '''
        1、转十进制相加
        2、转二进制: 除2取余，翻转
        '''
        s1, s2 = 0, 0
        l1, l2 = len(a), len(b)
        for i, item in enumerate(a):
            s1 += int(item) * 2 ** (l1 - 1 - i)
        for i, item in enumerate(b):
            s2 += int(item) * 2 ** (l2 - 1 - i)
        s = s1 + s2
        m = []
        if s == 0:
            return '0'
        while s != 0:
            m.append(str(s % 2))
            s = s // 2
        m.reverse()
        return ''.join(m)


if __name__ == '__main__':
    solu = Solution()
    # s1 = solu.addBinary2('11', '1')
    s = solu.addBinary3('11', '1')
    print(int(s))

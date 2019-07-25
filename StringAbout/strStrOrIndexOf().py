#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-03-03
  @Author  : Kaka
  @File    : strStrOrIndexOf().py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/implement-strstr/
  @Desc    : 实现strStr(),java中的indexof()
  实现 strStr() 函数。

    给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

    示例 1:

    输入: haystack = "hello", needle = "ll"
    输出: 2
    示例 2:

    输入: haystack = "aaaaa", needle = "bba"
    输出: -1
    说明:

    当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

    对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '' or needle == None: return 0
        return haystack.find(needle)

    def strStr_(self, haystack: str, needle: str) -> int:
        '''方案：1、获取needle长度n和第一个字符f
                2、从haystack找到所有f字符的索引，然后截取长度为n的字符串和needle比较
        '''
        if needle == '' or needle is None:
            return 0
        if haystack is None:
            return -1
        l1, l2 = len(haystack), len(needle)
        if l2 > l1: return -1
        firstc = needle[0]
        cindex = []
        for i, c in enumerate(haystack):
            if c == firstc:
                cindex.append(i)
        for i in cindex:
            if haystack[i:min(i + l2, l1)] == needle:
                return i
        return -1


if __name__ == '__main__':
    solu = Solution()
    haystack, needle = None, 'zz'
    print(solu.strStr_(haystack, needle))

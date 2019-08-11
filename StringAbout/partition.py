#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-03
  @Author  : Kaka
  @File    : partition.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/palindrome-partitioning/
  @Desc    : 分割回文串
  给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

    返回 s 所有可能的分割方案。

    示例:

    输入: "aab"
    输出:
    [
      ["aa","b"],
      ["a","a","b"]
    ]
"""


class Solution:
    def partition(self, s: str) :
        '''方案1：暴力解法，字符归并找到所有子集，在每一个进行判断
            1、分割一次，得到所有的满足子串是回文串的分割方式
        '''
        if len(s)==1:return [s]
        def ispalindrome(s):
            return s==s[::-1]
        sublist =[list(s)]
        def combine(ls):
            for i,w in enumerate(ls[:-1]):
                sublist.append(ls[:i]+[ls[i]+ls[i+1]]+ls[i+1+1:])
        for ls in sublist:
            combine(ls)
        result = []
        for item in sublist:
            for w in item:
                if not ispalindrome(w):
                    break
            else:
                result.append(item)
        result = [w.split('-') for w in set(['-'.join(item) for item in result])]
        return result

    def partition_(self,s):
        '''方案2：递归解法 TODO
        '''


    def _partition(self, s, index, t, result):
        if index == len(s):
            result.append(t.copy())
            return

        for i in range(index + 1, len(s) + 1):
            if s[index:i] == s[index:i][::-1]:
                t.append(s[index:i])
                self._partition(s, i, t, result)
                t.pop()

    def partition2(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = list()
        if not s:
            return result

        self._partition(s, 0, list(), result)
        return result

if __name__ == '__main__':
    solu =Solution()
    s = 'efe'
    result = solu.partition2(s)
    print(result)




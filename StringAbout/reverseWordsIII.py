#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-07-30
  @Author  : Kaka
  @File    : reverseWordsIII.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
  @Desc    : 反转字符串中的单词 III
  给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

    示例 1:

    输入: "Let's take LeetCode contest"
    输出: "s'teL ekat edoCteeL tsetnoc" 
    注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        '''题解：等于翻转字符串中的每个字符
        方案：双指针 TODO
        '''
        def reverseds(s, p, r):
            while p<r:
                s[p],s[r] = s[r],s[p]
            return s
        s = list(s.strip())
        p, r = 0, 0
        while r < len(s):
            for i, w in enumerate(s):
                if w != ' ':
                    r += 1
                elif p != r:
                    s = reverseds(s, p, r)
                    p = r
                else:
                    p += 1
                    r += 1
                print(s)

    def reverseWords_(self, s: str) -> str:
        '''调库:'''
        s = s.split()
        for i,w in enumerate(s):
            s[i] = w[::-1]
        return ' '.join(s)
if __name__ == '__main__':
    solu =Solution()
    s = "Let's take LeetCode contest"
    rs = solu.reverseWords_(s)
    assert rs=="s'teL ekat edoCteeL tsetnoc",'test error !!!!'

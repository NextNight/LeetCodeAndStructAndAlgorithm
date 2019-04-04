#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-02-27
  @Author  : Kaka
  @File    : findUniqueStr.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/first-unique-character-in-a-string/
  @Desc    : 字符串中的第一个唯一字符
  字符串中的第一个唯一字符
    给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

    案例:

    s = "leetcode"
    返回 0.

    s = "loveleetcode",
    返回 2.

    注意事项：您可以假定该字符串只包含小写字母。
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s==None or s=='':return -1
        if len(s)==1:return 0
        dis = {}
        for sx in s:
            if dis.get(sx) == None:
                dis[sx] = 1
            else:
                dis[sx] += 1
        min = 99999999
        for item in dis.items():
            if item[1]==1 and s.index(item[0]) < min:
                min =s.index(item[0])
        return min

if __name__ == '__main__':
    solu = Solution()
    print(solu.firstUniqChar('loveleetcode'))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-03
  @Author  : Kaka
  @File    : groupAnagrams.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/group-anagrams/
  @Desc    : 字母异位词分组
  给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

    示例:

    输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
    输出:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    说明：

    所有输入均为小写字母。
    不考虑答案输出的顺序。
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """O(n),O(n)
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i,str in enumerate(strs):
            sstr = ''.join(sorted(str))
            if dic.get(sstr)==None:
                dic[sstr] =[i]
            else:
                dic[sstr].append(i)
        rs = []
        for k in dic:
            rs.append([ strs[i] for i in dic[k]])

        print(dic.values())

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solu = Solution()
    solu.groupAnagrams(strs)



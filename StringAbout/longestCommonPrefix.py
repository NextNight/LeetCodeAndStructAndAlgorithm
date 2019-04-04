#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-03-03
  @Author  : Kaka
  @File    : longestCommonPrefix.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/longest-common-prefix/
  @Desc    : 最长公共前缀
    编写一个函数来查找字符串数组中的最长公共前缀。

    如果不存在公共前缀，返回空字符串 ""。

    示例 1:

    输入: ["flower","flow","flight"]
    输出: "fl"
    示例 2:

    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。
    说明:

    所有输入只包含小写字母 a-z 。

"""
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> str:
        if len(strs)<1: return ""
        min_len = min([len(s) for s in strs])
        longpf=""
        for i in range(min_len):
            if len(set([strs[j][i] for j in range(len(strs))]))==1:
                longpf+=strs[0][i]
            else:
                break
        return longpf

if __name__ == '__main__':
    strs = ["flower","flow","flight"]#["dog","racecar","car"]
    solu = Solution()
    print(solu.longestCommonPrefix(strs))




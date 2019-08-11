#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-06
  @Author  : Kaka
  @File    : wordBreak.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/word-break/
  @Desc    :  单词拆分
  给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

    说明：

    拆分时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。
    示例 1：

    输入: s = "leetcode", wordDict = ["leet", "code"]
    输出: true
    解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
    示例 2：

    输入: s = "applepenapple", wordDict = ["apple", "pen"]
    输出: true
    解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
         注意你可以重复使用字典中的单词。
    示例 3：

    输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    输出: false

"""


class Solution:
    def wordBreak(self, s,wordDict) -> bool:
        '''方案：从头遍历s,查看第一个字符是否在wordDict，否则查看前两个，否则前三个。知道整个s FIXME:错误❎,
        '''
        wordDict = sorted(wordDict)
        rm = []
        # for i,item in enumerate(wordDict[:-1]):
        #     if wordDict[i+1].count(item)>0:
        #         rm.append(item)
        # for item in rm :
        #     wordDict.remove(item)
        print(wordDict)
        def prevs(ss):
            if ss in wordDict:
                return True
            for i in  range(0,len(ss)):
                if ss[:i] in wordDict:
                    return prevs(ss[i:])
        return prevs(s)

if __name__ == '__main__':
    solu =Solution()
    s = "goalspecial"
    wordDict =  ["go","goal","goals","special"]
    print(solu.wordBreak(s,wordDict))


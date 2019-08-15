#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-12
  @Author  : Kaka
  @File    : validParentheses.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/valid-parentheses
  @Desc    : 有效的括号
  给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。

    示例 1:

    输入: "()"
    输出: true
    示例 2:

    输入: "()[]{}"
    输出: true
    示例 3:

    输入: "(]"
    输出: false
    示例 4:

    输入: "([)]"
    输出: false
    示例 5:

    输入: "{[]}"
    输出: true

"""


class Solution:
    def isValid(self, s: str) -> bool:
        '''有效的括号:
        方案：用栈
        '''
        dic = {'(':')','{':'}','[':']'}
        if s is None or s=='':
            return True
        ss = list(s)
        stack = [ss[0]]
        for i,item in enumerate(ss[1:]):
            if len(stack)>0 and item==dic.get(stack[-1]):
                stack.pop()
            else:
                stack.append(item)
        if len(stack)==0:
            return True
        return False

if __name__ == '__main__':
    solu = Solution()
    print(solu.isValid('{[]}'))



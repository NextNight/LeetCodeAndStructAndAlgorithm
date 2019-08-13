#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-13
  @Author  : Kaka
  @File    : decodeString.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/decode-string/
  @Desc    : 字符串解码
  给定一个经过编码的字符串，返回它解码后的字符串。

    编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

    你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

    此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

    示例:

    s = "3[a]2[bc]", 返回 "aaabcbc".
    s = "3[a2[c]]", 返回 "accaccacc".
    s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
"""


class Solution:
    def decodeString(self, s: str) -> str:
        '''字符串解码：
        方案：类似括号匹配，只不过对于匹配上的括号要将其前面的数字✖这个括号内的字符串再入栈
            1、顺序入栈，直到遇到‘]’，
            2、开始出栈,出栈字符拼接，直到遇到'['，再出栈一个得到的就是数字
            3、用这个数字去重复拼接的字符得到一个括号解码，入栈，
            4、继续重复1，2，3
            5、遍历完字符，把栈中所有字符逆序拼接
        '''
        stack, result = [], ''
        for item in s:
            if item == ']':
                es, num = '', ''
                while True:
                    if stack[-1] != '[':
                        es = stack.pop() + es
                    else:
                        stack.pop()
                        while len(stack) > 0 and stack[-1].isnumeric():
                            num = stack.pop() + num
                        break
                es = es * int(num)
                stack.append(es)
            else:
                stack.append(item)

        while stack:
            result = stack.pop() + result
        print(result)
        return result


if __name__ == '__main__':
    solu = Solution()
    s = "3[a]2[bc]"
    assert solu.decodeString(s) == "aaabcbc"

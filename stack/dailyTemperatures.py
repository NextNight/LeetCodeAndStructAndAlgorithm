#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-12
  @Author  : Kaka
  @File    : dailyTemperatures.py
  @Software: PyCharm
  @Contact : 
  @Desc    : 每日气温
  根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
    例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

    提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""


class Solution:
    def dailyTemperatures(self, T):
        if T is None:
            return None
        if len(T) == 1:
            return [0]
        stack = [(T[0], 0)]
        rs = [0] * len(T)

        def cstack(i, num):
            if len(stack) > 0 and stack[-1][0] < num:
                rs[stack[-1][1]] = (i - stack[-1][1])
                stack.pop()
                cstack(i, num)

        for i, item in enumerate(T[1:]):
            if len(stack) > 0 and stack[-1][0] < item:
                cstack(i + 1, item)
            stack.append((item, i + 1))
        return rs


if __name__ == '__main__':
    solu = Solution()
    t = [73, 74, 75, 71, 69, 72, 76, 73]
    solu.dailyTemperatures(t)

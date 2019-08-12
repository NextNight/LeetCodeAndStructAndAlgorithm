#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-12
  @Author  : Kaka
  @File    : evaluateReversePolishNotation.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
  @Desc    : 逆波兰表达式求值
  根据逆波兰表示法，求表达式的值。

    有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

    说明：

    整数除法只保留整数部分。
    给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
    示例 1：

    输入: ["2", "1", "+", "3", "*"]
    输出: 9
    解释: ((2 + 1) * 3) = 9
    示例 2：

    输入: ["4", "13", "5", "/", "+"]
    输出: 6
    解释: (4 + (13 / 5)) = 6
    示例 3：

    输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    输出: 22
    解释:
      ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22

"""


class Solution:
    def evalRPN(self, tokens) -> int:
        '''逆波兰式求值：
        方案：顺序入栈，遇到操作符取栈顶两元素进行操作结果入栈，直到所有的输入入栈完成，操作符操作完成得到求值
        '''
        opter = ['+','-','*','/']
        stack = []
        for t in tokens:
            if t in opter:
                t2 = stack.pop()
                t1 = stack.pop()
                stack.append(int(eval(str(t1)+t+str(t2))))
            else:
                stack.append(t)
        return stack[-1]

if __name__ == '__main__':
    solu = Solution()
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    solu.evalRPN(tokens)





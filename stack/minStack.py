#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-12
  @Author  : Kaka
  @File    : minStack.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/min-stack/
  @Desc    : 最小栈
    设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

    push(x) -- 将元素 x 推入栈中。
    pop() -- 删除栈顶的元素。
    top() -- 获取栈顶元素。
    getMin() -- 检索栈中的最小元素。
    示例:

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.getMin();   --> 返回 -2.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        if self.data == []:
            self.data.append((x, x))
        else:
            self.data.append((x, min(self.getMin(),x)))

    def pop(self) -> None:
        if self.data == []:
            pass
        else:
            return self.data.pop()


    def top(self) -> int:
        if self.data==[]:
            return -1
        return self.data[-1][0]

    def getMin(self) -> int:
        if self.data==[]:
            return -1
        return self.data[-1][1]
if __name__ == '__main__':
    minstack = MinStack()
    minstack.push(-2)
    minstack.push(0)
    minstack.push(-1)
    print(minstack.getMin())
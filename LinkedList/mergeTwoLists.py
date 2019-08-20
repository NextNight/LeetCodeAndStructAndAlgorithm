#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-19
  @Author  : Kaka
  @File    : mergeTwoLists.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/merge-two-sorted-lists/
  @Desc    : 合并两个有序链表
    将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

    示例：

    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val<=l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

if __name__ == '__main__':
    solu = Solution()
    solu.mergeTwoLists()
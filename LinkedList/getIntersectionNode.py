#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-09-04
  @Author  : Kaka
  @File    : getIntersectionNode.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
  @Desc    : 相交链表
  编写一个程序，找到两个单链表相交的起始节点。
    注意：

    如果两个链表没有交点，返回 null.
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。


"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        方案：消除长度差，即较短的那个链表，因为相交部分是相同长度
        """
        A, B = headA, headB
        while headA != headB:
            if headA and headB:
                headA = headA.next
                headB = headB.next
            elif headB and not headA:
                headB = headB.next
                B=B.next
            elif headA and not headB:
                headA = headA.next
                A=A.next
        while A!=B:
            A=A.next
            B=B.next
        return A

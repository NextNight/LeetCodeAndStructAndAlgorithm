#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-15
  @Author  : Kaka
  @File    : swapPairs.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/swap-nodes-in-pairs/
  @Desc    : 两两交换链表中的节点
  给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


    示例:

    给定 1->2->3->4, 你应该返回 2->1->4->3.

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        '''递归'''
        if head is None or head.next is None:
            return head
        h=head.next
        head.next=self.swapPairs(head.next.next)
        h.next=head
        return h

if __name__ == '__main__':
    N1 =ListNode(1)
    N2 =ListNode(2)
    N3 =ListNode(3)
    N4 =ListNode(4)
    N1.next=N2
    N2.next=N3
    N3.next=N4
    solu =Solution()
    head =solu.swapPairs(N1)
    while head:
        print(head.val)
        head =head.next
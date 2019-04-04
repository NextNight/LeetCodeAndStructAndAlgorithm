#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 
  @Author  : chengxin
  @File    : reserseList.py
  @Software: PyCharm
  @Contact : 1031329190@qq.com
  @Desc    :
  反转一个单链表。

    示例:

    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
    进阶:
    你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#%%
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        hhead = ListNode(0)
        hhead.next = head
        cur = head.next
        head.next=None
        while cur!=None:
            node = cur
            cur = cur.next
            node.next=hhead.next
            hhead.next =node
        return hhead.next
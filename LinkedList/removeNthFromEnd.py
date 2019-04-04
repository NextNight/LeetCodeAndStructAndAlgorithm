#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 
  @Author  : chengxin
  @File    : removeNthFromEnd.py
  @Software: PyCharm
  @Contact : 1031329190@qq.com
  @Desc    :
  给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

    示例：
        给定一个链表: 1->2->3->4->5, 和 n = 2.
        当删除了倒数第二个节点后，链表变为 1->2->3->5.
    说明：
        给定的 n 保证是有效的。
    进阶：
        你能尝试使用一趟扫描实现吗？
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    '''删除第倒数第n个节点关键在于如何找到倒数第n+1个节点也就是倒数n节点的前驱：
        当我们遍历链表到第n+1个节点的时候那个第一个节点就是倒数第n+1个节点，
        用一个指针H指向第一个节点，然后和当前指针保持相对位置，当前指针移到末尾，那么H就指向了倒数n+1'''
    hd = ListNode(0)
    f = hd
    s = hd
    i = 1
    while f!=None:
        if i<=n+1:
            i+=1
            f = f.next
        else:
            s = s.next
            f = f.next
    s.next=s.next.next
    return hd.next

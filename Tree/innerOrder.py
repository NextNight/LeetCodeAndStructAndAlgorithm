#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-02-22
  @Author  : Kaka
  @File    : innerOrder.py
  @Software: PyCharm
  @Contact : 
  @Desc    : 中序遍历
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def innerOrder(root,innerList):
    '''中序遍历'''
    if root==None:return
    innerOrder(root.left,innerList)
    innerList.append(root.val)
    innerOrder(root.left,innerList)

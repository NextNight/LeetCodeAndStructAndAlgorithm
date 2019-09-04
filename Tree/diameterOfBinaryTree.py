#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-09-04
  @Author  : Kaka
  @File    : diameterOfBinaryTree.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/diameter-of-binary-tree/
  @Desc    : 二叉树的直径
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    dis = 0
    def diameterOfBinaryTree(self, root):
        """
        方案：最大直径==左子树最大深度+右字数最大深度-1
        """
        def deep(root):
            if root is None: return 0
            l = deep(root.left)
            r = deep(root.right)
            self.dis = max(l+r,self.dis)
            return max(l,r)+1
        deep(root)
        return self.dis

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-02-22
  @Author  : Kaka
  @File    : levleOrder.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
  @Desc    : 层次遍历
    给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

    例如:
    给定二叉树: [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    返回其层次遍历结果：

    [
      [3],
      [9,20],
      [15,7]
    ]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def leveNode(nodes):
            dts = []
            for node in nodes:
                if node.left:
                    dts.append(node.left)
                if node.right:
                    dts.append(node.right)
            return dts

        dt, rs = [], []
        if root == None:
            return []
        else:
            dt.append(root)
        while len(dt) > 0:
            rs.append([node.val for node in dt])
            dt = leveNode(dt)
        return rs
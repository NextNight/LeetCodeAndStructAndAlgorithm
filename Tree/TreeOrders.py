#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-02-22
  @Author  : Kaka
  @File    : TreeOrders.py
  @Software: PyCharm
  @Contact : 
  @Desc    : 树的各种遍历
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeOrder(object):
    def prevOrder(self, root: TreeNode, order_list):
        '''先序遍历'''
        if root == None: return
        order_list.append(root.val)
        self.prevOrder(root.left, order_list)
        self.prevOrder(root.right, order_list)

    def innerOrder(self, root: TreeNode, order_list):
        '''中序遍历'''
        if root == None: return
        self.innerOrder(root.left, order_list)
        order_list.append(root.val)
        self.innerOrder(root.left, order_list)

    def postOrder(self, root: TreeNode, order_list):
        '''后序遍历'''
        if root == None: return
        self.postOrder(root.left, order_list)
        self.postOrder(root.right, order_list)
        order_list.append(root.val)

    def levleOrder(self, root: TreeNode, order_list):
        '''层次遍历'''
        node_list = []
        if root == None:
            return
        else:
            node_list.append(root)

        def nextNodes(node_list):
            nodes = []
            for node in node_list:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            return nodes

        while len(node_list) > 0:
            order_list.append([node.val for node in node_list])
            node_list = nextNodes(node_list)

    def maxDepth(self, root: TreeNode):
        '''二叉树的最大深度'''
        if root == None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height,right_height)+1

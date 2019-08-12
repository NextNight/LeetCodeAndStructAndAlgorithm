#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-12
  @Author  : Kaka
  @File    : maxDepth.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
  @Desc    : 二叉树的最大深度
    给定一个二叉树，找出其最大深度。

    二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

    说明: 叶子节点是指没有子节点的节点。

    示例：
    给定二叉树 [3,9,20,null,null,15,7]，

        3
       / \
      9  20
        /  \
       15   7
    返回它的最大深度 3 。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth_v1(self, root: TreeNode) -> int:
        '''二叉树的最大深度:
        方案：DFS递归解法，二叉树的最大深度==其左子树和右子树最大高度+1(根节点)
        '''
        if root == None:
            return 0
        left_height = self.maxDepth_v1(root.left)
        right_height = self.maxDepth_v1(root.right)
        return max(left_height, right_height) + 1

    def maxDepth_v2(self, root: TreeNode) -> int:
        '''二叉树的最大深度:
            DFS:深度优先算法,使用栈保存每个节点的Node和其深度
        '''
        if root == None:
            return 0
        stack, max_height = [(root, 1)], 0
        while stack:
            node, height = stack.pop()
            max_height = max(max_height, height)
            if node.left:
                stack.append((node.left, height + 1))
            if node.right:
                stack.append((node.right, height + 1))
        return max_height

    def maxDepth_v3(self, root: TreeNode) -> int:
        '''二叉树的最大深度:
            BFS:广度优先算法,使用队列保存每个节点的Node和其深度
        '''
        if root == None:
            return 0
        queue, max_height = [(root, 1)], 0
        while queue:
            node,height = queue.pop(0)
            max_height = max(max_height,height)
            if node.left:
                queue.append((node.left, height + 1))
            if node.right:
                queue.append((node.right, height + 1))
        return max_height

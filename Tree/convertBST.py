#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-08-21
  @Author  : Kaka
  @File    : convertBST.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
  @Desc    : 把二叉搜索树转换为累加树
  给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

    例如：

    输入: 二叉搜索树:
                  5
                /   \
               2     13

    输出: 转换为累加树:
                 18
                /   \
              20     13

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        '''方案：中序遍历
        '''
        self.num = 0
        def inner_order(root):
            if root is None:
                return
            inner_order(root.right)
            self.num+=root.val
            root.val=self.num
            inner_order(root.left)
        inner_order(root)

    def convertBST_v2(self, root: TreeNode) -> TreeNode:
        '''方案：中序遍历，逆序叠加
        '''
        order_list =[]
        def inner_order(root,order_list):
            if root is None:
                return None
            inner_order(root.right,order_list)
            order_list.append(root)
            inner_order(root.left,order_list)
        inner_order(root,order_list)
        num =0
        for i,node in enumerate(order_list):
            num = num+node.val
            node.val=num

if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(5)
    N1 = TreeNode(2)
    N2 = TreeNode(13)
    root.left=N1
    root.right=N2
    solu.convertBST(root)
    print(root.val,root.left.val,root.right.val)

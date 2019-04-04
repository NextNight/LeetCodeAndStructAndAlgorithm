#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-02-22
  @Author  : Kaka
  @File    : isValidBST.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/validate-binary-search-tree/
  @Desc    :
  给定一个二叉树，判断其是否是一个有效的二叉搜索树。

    假设一个二叉搜索树具有如下特征：

    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
    示例 1:

    输入:
        2
       / \
      1   3
    输出: true
    示例 2:

    输入:
        5
       / \
      1   4
         / \
        3   6
    输出: false
    解释: 输入为: [5,1,4,null,null,3,6]。
         根节点的值为 5 ，但是其右子节点值为 4
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        '''
        题目: 是否是二叉搜索树
        思路：如果满足二叉搜索树的特点，那么中序遍历一定是一个升序序列，则先进行中序遍历，结果在进行是否是升序判断。
        '''
        innerList = []
        def innerOrder(root, innerList):
            '''中序遍历'''
            if root == None:
                return
            innerOrder(root.left,innerList)
            innerList.append(root.val)
            innerOrder(root.left,innerList)
        innerOrder(root,innerList)
        for i,nv in enumerate(innerList[:-1]):
            if nv>=innerList[i+1]:
                return False
        return True
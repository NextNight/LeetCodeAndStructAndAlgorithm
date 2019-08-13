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
    def prevOrder_v1(self, root: TreeNode, order_list):
        '''先序遍历：递归解法'''
        if root == None: return
        order_list.append(root.val)
        self.prevOrder_v1(root.left, order_list)
        self.prevOrder_v1(root.right, order_list)
        print(order_list)

    def prevOrder_v2(self, root: TreeNode, order_list):
        '''先序遍历：迭代解法'''
        if root == None: return
        stack = [root]
        while stack:
            node = stack.pop()
            order_list.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print(order_list)

    def innerOrder_v1(self, root: TreeNode, order_list):
        '''中序遍历:递归解法'''
        if root == None: return
        self.innerOrder_v1(root.left, order_list)
        order_list.append(root.val)
        self.innerOrder_v1(root.right, order_list)
        print(order_list)

    def innerOrder_v2(self, root: TreeNode, order_list):
        '''中序遍历：迭代解法'''
        if root == None: return
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            order_list.append(curr.val)
            curr = curr.right
        print(order_list)

    def postOrder_v1(self, root: TreeNode, order_list):
        '''后序遍历'''
        if root == None: return
        self.postOrder_v1(root.left, order_list)
        self.postOrder_v1(root.right, order_list)
        order_list.append(root.val)

    def postOrder_v2(self, root: TreeNode, order_list):
        '''后序遍历：迭代解法 TODO'''
        if root == None: return

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
        return max(left_height, right_height) + 1


if __name__ == '__main__':
    toder = TreeOrder()
    order_list = []
    na = TreeNode('A')
    nb = TreeNode('B')
    nc = TreeNode('C')
    nd = TreeNode('D')
    ne = TreeNode('E')
    nf = TreeNode('F')
    na.left = nb
    na.right = nc
    nb.left = nd
    nb.right = ne
    nc.left = nf

    # toder.prevOrder_v1(root=na,order_list=order_list)
    # toder.prevOrder_v2(root=na, order_list=order_list)
    # toder.innerOrder_v1(root=na, order_list=order_list)
    toder.innerOrder_v2(root=na, order_list=order_list)

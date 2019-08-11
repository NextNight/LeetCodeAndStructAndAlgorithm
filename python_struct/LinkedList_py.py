#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 
  @Author  : chengxin
  @File    : 
  @Software: PyCharm
  @Contact :
  @Desc    : python实现链表
"""


class Node(object):
	"""定义链表的节点"""

	def __init__(self, data):
		self._data = data
		self._next = None


class LinkedList(object):
	def __init__(self):
		self._head = Node(None)
		self._tail = Node(None)
		self._head._next=self._tail
		self._size = 0

	def add(self, data):
		"""头插法：新加入的元素永远在head._next"""
		node = Node(data)
		node._next = self._head._next
		self._head._next = node

		self._size += 1

	def remove(self, data):
		"""删除节点"""
		prev = self._head
		while prev._next is not self._tail:
			cur = prev._next
			if cur._data() == data:
				prev._next = cur._next

		self._size -=1

	def size(self):
		return self._size

	def is_exist(self, data):
		"""查询某值是否在链表"""
		if any([self._head._next == self._tail, data == None]):
			return False
		cur = self._head._next
		while cur is not self._tail:
			if cur.get_data == data:
				return True
			else:
				return False

	def is_empty(self):
		return self._head._next == self._tail

	def foreach(self):
		if self._head._next == self._tail:
			return None
		data = []
		cur = self._head._next
		while cur is not self._tail:
			data.append(cur._data)
			cur = cur._next
		return data

if __name__ == '__main__':
	linkedlist = LinkedList()
	linkedlist.add(1)
	linkedlist.add(2)
	linkedlist.add(3)
	print(linkedlist.foreach())
	print(linkedlist.size())

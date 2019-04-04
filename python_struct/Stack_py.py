#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 
  @Author  : chengxin
  @File    : 
  @Software: PyCharm
  @Contact : 1031329190@qq.com
  @Desc    : python 实现栈
"""


class Stack_imp_array(object):
	'''数组实现'''
	def __init__(self, init_size):
		self._data = [0] * init_size
		self._top = 0
		self._size = init_size

	def isempty(self):
		return self._top==0

	def push(self, item):
		if self._top>=self._size-1:
			print("stack full")
		else:
			self._top += 1
			self._data[self._top] = item

	def pop(self):
		if self.isempty():
			print("stack empty")
			return None
		else:
			top = self._data[self._top]
			self._top -= 1
			return top

	def foreach(self):
		rs = []
		while self._top !=0:
			top = self.pop()
			rs.append(top)
		return rs

class Node(object):
	"""定义链表的节点"""
	def __init__(self, data):
		self.data_ = data
		self.next_ = None

class Stack_imp_linkedlist(object):
	'''链表实现栈'''
	def __init__(self,):
		self.Link = Node(None)
		self.top = None
		self.len = 0

	def push(self,item):
		p = Node(item)
		p.next_=self.Link.next_
		self.Link.next_=p
		self.top=p
		self.len+=1

	def pop(self):
		if self.len>0:
			data = self.top.data_
			self.Link.next_ = self.top.next_
			self.top = self.Link.next_
			self.len-=1
			return data
		else:
			print('Stack empty')
			return None

if __name__ == '__main__':
	stack = Stack_imp_linkedlist()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	# print(stack.foreach())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 
  @Author  : chengxin
  @File    : 
  @Software: PyCharm
  @Contact :
  @Desc    : python实现队列
"""


class Queue(object):
	'''顺序队列'''
	def __init__(self, init_size):
		self._data = [None] * init_size
		self._head = -1
		self._tail = -1
		self._size = init_size

	def isFull(self):
		return self._tail>=self._size-1

	def isEmpty(self):
		return self._tail<=self._head


	def enQueue(self, item):
		if self.isFull():
			print("queue full")
		else:
			self._tail += 1
			self._data[self._tail] = item


	def deQueue(self):
		if self.isEmpty():
			print("queue empty")
		else:
			self._head += 1
			top = self._data[self._head]
			self._data[self._head] = None
			return top

	def foreach(self):
		rs = []
		while self._head <= self._tail-1:
			top = self.deQueue()
			rs.append(top)
		return rs


if __name__ == '__main__':
	queue = Queue(5)
	queue.enQueue(1)
	queue.enQueue(2)
	queue.enQueue(3)
	queue.enQueue(4)
	queue.enQueue(5)
	print(queue.foreach())

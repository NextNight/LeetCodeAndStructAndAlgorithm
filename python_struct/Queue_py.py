#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 
  @Author  : chengxin
  @File    : 
  @Software: PyCharm
  @Contact : 1031329190@qq.com
  @Desc    : python实现队列
"""


class Queue(object):
	def __init__(self, init_size):
		self._data = [None] * init_size
		self._head = -1
		self._tail = -1
		self._size = init_size

	def add(self, item):
		if self._tail >= self._size-1:
			print("queue full")
		else:
			self._tail += 1
			self._data[self._tail] = item


	def poll(self):
		if self._head >= self._tail:
			print("queue empty")
		else:
			self._head += 1
			top = self._data[self._head]
			self._data[self._head] = None
			return top

	def foreach(self):
		rs = []
		while self._head <= self._tail-1:
			top = self.poll()
			rs.append(top)
		return rs


if __name__ == '__main__':
	queue = Queue(5)
	queue.add(1)
	queue.add(2)
	queue.add(3)
	queue.add(4)
	queue.add(5)
	print(queue.foreach())

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
        return self._tail >= self._size - 1

    def isEmpty(self):
        return self._head >= self._tail

    def enQueue(self, item):
        if self.isFull():
            print("queue full")
            return False
        self._tail += 1
        self._data[self._tail] = item
        return True

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
        while self._head <= self._tail - 1:
            top = self.deQueue()
            rs.append(top)
        return rs


class MyCircularQueue:
    '''循环队列'''

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = [0] * k
        self.head = -1
        self.tail = -1
        self.size = k

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.tail + 1) % self.size == self.head

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.data[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if (self.head == self.tail):
            self.head = -1
            self.tail = -1
            return True
        self.head = (self.head + 1) % self.size
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.isEmpty():
            return self.data[self.head]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.isEmpty():
            return self.data[self.head]
        else:
            return -1



if __name__ == '__main__':
    queue = Queue(5)
    queue.enQueue(1)
    queue.enQueue(2)
    queue.enQueue(3)
    queue.enQueue(4)
    queue.enQueue(5)
    queue.deQueue()
    queue.deQueue()
    queue.deQueue()
    queue.deQueue()
    queue.deQueue()
    queue.deQueue()
    print(queue.foreach())

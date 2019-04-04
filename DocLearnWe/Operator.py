#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 
  @Author  : chengxin
  @File    : 
  @Software: PyCharm
  @Contact : 1031329190@qq.com
  @Desc    : 位运算相关的算法
"""
"""
a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100 # & 全1为1
 
a|b = 0011 1101 # | 有1为1

a^b = 0011 0001 # ^ 相同为0，相异为1

~a  = 1100 0011 # ~ 取反

<<  			# 左移
>>              # 右移
"""

# 位运算相关题目
"""1、不使用交换空间交换两个数"""
def swap_1(num1, num2):
	"""不使用交换空间交换两个数"""
	num1 = num1 ^ num2
	num2 = num1 ^ num2
	num1 = num1 ^ num2
	return num1, num2


def swap_2(num1, num2):
	"""以上的简化版"""
	num1 ^= num2
	num2 ^= num1
	num1 ^= num2
	return num1, num2


"""2、计算一个数的二进制表示有几个1"""
def count_one(num):
	count = 0
	while num != 0:
		num &= (num - 1)
		count += 1
	return count


"""3、交换二进制i，j位上的值"""
def swap_bin(num, i, j):
	"""x&1 表示最后一位是什么
	(0b0000110 >> 1) &1 # 1
	(0b0000110 >> 2) &1 # 1
	(0b0000110 >> 3) &1 # 0

	(1 << num) | (1 << j)表示交换i,j的值
	"""
	if (num >> i) & 1 != (num >> j) & j:
		num = num ^ (1 << num) | (1 << j)

	return num

if __name__ == '__main__':
	print(count_one(12))

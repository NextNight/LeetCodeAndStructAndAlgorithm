#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 
  @Author  : chengxin
  @File    : 
  @Software: PyCharm
  @Contact : 1031329190@qq.com
  @Desc    : 
"""


def insert_sort(nums):
	'''插入排序
	思路：1、将数据分成两部分，一部分是有序L，一部分是无序R,
		 2、将有序的尾指针指向无序的头，然后从后往前遍历，将这个无序数据找到合适的位置，然后再将指针指向下一个元素
		 3、重复2步骤，知道指针指向最后一个元素并完成寻找位置为止。
	'''
	if len(nums) <= 1 or nums == None:
		return nums
	for i in range(1,len(nums)):
		for j in range(i, 0, -1):
			if nums[j] < nums[j-1]:
				nums[j-1],nums[j] = nums[j],nums[j-1]
	return nums

if __name__ == '__main__':
	nums = [6, 3, 2, 4, 1]
	print(insert_sort(nums))

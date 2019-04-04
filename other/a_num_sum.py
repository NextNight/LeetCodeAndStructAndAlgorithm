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
import sys
import math
import numpy as np


def a_num_sum(num):
    """
    Q: 给一个非负整数，求每一位的数字加和，得到之后的数字在把每一位进行加和，直到结果为一位数
    E: 比如：83->8+3=11->1+1=2,输出2
    case: 尾递归，进入下一层不再需要上一层的环境，因为这个递归完成后不再需要干其他的事，所以直接return这个递归，就会得到最内层的结果
    """
    # 如果要输出每次计算的值
    # print(num)   # 83 11 2
    # if num >= 10:
    #     a_num_sum(sum([int(i) for i in list(str(num))]))
    # print(num)  # 2,11,83

    if num < 10:
        return num
    if num >= 10:
        return a_num_sum(sum([int(i) for i in list(str(num))]))


def two_sum(dt, tag):
    """
    Q:给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
    E:[2,7,3,11] tag:9
    """
    # for i, item in enumerate(dt):
    #     if (tag - item) in dt and dt.index(tag - item)!=i:
    #         return [i, dt.index(tag - item)]

    for i, it in enumerate(dt):
        for j, jt in enumerate(dt):
            if it + jt == tag and i != j:
                return [i, j]

    # dict 不能存k相同的键值对,python中没有hashmap
    # dic={}
    # for i, it in enumerate(dt):
    #     dic[it]=i
    #     ti = dic.get(tag-it)
    #     if  ti !=None and ti !=i:
    #         return [i,ti]


def reverse(num):
    """整数翻转"""
    """
    Q:给定一个 32 位有符号整数，将整数中的数字进行反转。假设我们的环境只能存储 32 位有符号整数，
    其数值范围是 [−2**31,  2**31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
    """
    sum = 0
    while True:
        lens = len(str(num)) - 1
        sum += (num % 10) * 10 ** lens
        num = int(num / 10)
        if lens == 0:
            if sum < -2 ** 31 or sum > 2 ** 31 - 1:
                return 0
            return sum


def max_sum_subarry(nums):
    """子串最大和"""
    """
    Q:给定一个数组求其子数组和最大的值。
    E:[1, -2, 3, 10, -4, 7, 2, -5]
    R:[3,10,-4,7,2]=18
    
    trick: 动态规划
    """

    if nums is None:
        return None
    if len(nums) == 1:
        return nums[0]
    sum = nums[0]  # 第i-1个数的最大序列和
    cur = nums[0]  # 第i个数的最大序列和
    for i, it in enumerate(nums[1:]):
        cur = max(cur + it, it)  # 状态方程：max(sum_i) = max(sum_i-1+num[i],num[i])
        if sum < cur:
            sum = cur
    return sum


def max_subarray(nums):
    """最大和的子串"""
    """
    Q:给定一个数组求其子数组和最大的值。
    E:[1, -2, 3, 10, -4, 7, 2, -5]
    R:[3,10,-4,7,2]=18
    trick: 动态规划
    """
    if nums is None:
        return 0
    if len(nums) == 1:
        return nums[0]
    sum = nums[0]  # 第i-1个数的最大序列和
    cur = nums[0]  # 第i个数的最大序列和
    maxls = [nums[0]]  # 用于和最大的子序列
    for i, it in enumerate(nums[1:]):
        # cur = max(cur + it, it) # 状态方程：max(sum_i) = max(sum_i-1+num[i],num[i])
        if cur + it >= it:
            cur = cur + it
            maxls.append(it)
        else:
            cur = it
            maxls = [it]
        if sum < cur:
            sum = cur
    # 去掉子序列尾部的负数
    while maxls[-1] < 0:
        maxls.pop(-1)
    return sum, maxls


def max_stock(nums):
    """股票最大利润："""
    """
    A:https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。如果你最多只允许完成一笔交易（即买入和卖出一支股票），
    设计一个算法来计算你所能获取的最大利润
    E:[7,1,5,3,6,4]
    R:[1,6] = 5
    E:[7,6,4,3,1]
    R:0
    思路：记录最小值，和最大利润，不断用当前值-最小值去计算利润，如果大于最大利润则更新。保证当前值永远在最小值之后，因为卖出时间必须晚于或等于买入时间
    """
    if len(nums) == 1:
        return 0
    mins =  2**31
    stock = 0
    for it in nums[1:]:
        mins = min(it,mins)
        stock = max(it-mins,stock)
    return stock

def max_stock_all(nums):
    """股票最大利润：购买多次不限次数"""
    """
    E:[7,1,5,3,6,4]
    R:5-1+6-3=7
    思路：找到所有的上升区域，每个区域的差值之和就是总利润。
    """
    if len(nums)==1 or nums==None:
        return 0
    stock = 0
    min = nums[0]
    for it in nums[1:]:
        if it>min:
            stock +=it-min
        min = it
    return stock


def max_stock_two():
    """股票最大利润：智能购买2次"""
    """
    E:[7,1,5,3,6,4]
    R:5-1+6-3=7
    思路：找到所有的上升区域，每个区域的差值之和就是总利润。
    """
    pass


def transpose(A):
    """转置矩阵:2018-08-07"""
    """
    E:[[1,2,3],[4,5,6]]
    R:[[1,4],[2,5],[3,6]]
    """
    # r行，c列 转置得到c行r列
    r,c = len(A),len(A[0])
    # 定义一个c,行r列的矩阵
    rs = [ [None]*r for i in np.arange(c)]
    for r,row in enumerate(A):
        for c,it in enumerate(row):
            rs[c][r] = it
    return rs




if __name__ == '__main__':
    print(a_num_sum(83))
    print(two_sum([3, 3], 6))
    print(reverse(1234567891313))
    print(max_sum_subarry([1, -2, 3, 10, -4, 7, 2, -5]))
    print(max_subarray([1, -2, 3, 10, -4, 7, 2, -5, ]))
    print(max_stock([7,1,5,3,6,4]))
    print(max_stock_all([7,1,5,3,6,4]))
    print(max_stock_all([7,6,5,4,3,2]))
    print(transpose([[1,2,3],[4,5,6]]))
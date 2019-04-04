#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-02-26
  @Author  : Kaka
  @File    : maxProfit.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
  @Desc    : 买股票的最大利润
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

    如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

    注意你不能在买入股票前卖出股票。

    示例 1:

        输入: [7,1,5,3,6,4]
        输出: 5
        解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
             注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
    示例 2:

        输入: [7,6,4,3,1]
        输出: 0
        解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""
'‘’前i天的最大收益 = max(第i天价格-前i-1天的最小价格，第i-1天的最大收益)‘’'


class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        if prices == None or len(prices) <= 1: return 0
        i = len(prices)
        return max(prices[i - 1] - min(prices[:i - 1]), self.maxProfit(prices[:i - 1]))

    def maxProfit_2(self, prices: 'List[int]') -> int:
        '''递推'''
        if prices == None or len(prices) <= 1: return 0
        max_p, min_v = 0, 999999
        for i in range(len(prices)):
            max_p = max((prices[i] - min_v), max_p)
            min_v = min(min_v, prices[i])
        return max_p


if __name__ == '__main__':
    prices = [3, 7, 1, 5, 3, 6, 9]
    solu = Solution()
    print(solu.maxProfit_2(prices))

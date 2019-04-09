#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-04-09
  @Author  : Kaka
  @File    : dominantIndex.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/
  @Desc    : 至少是其他数字两倍的最大数
  在一个给定的数组nums中，总是存在一个最大元素 。

    查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

    如果是，则返回最大元素的索引，否则返回-1。

    示例 1:

    输入: nums = [3, 6, 1, 0]
    输出: 1
    解释: 6是最大的整数, 对于数组中的其他整数,
    6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.


    示例 2:

    输入: nums = [1, 2, 3, 4]
    输出: -1
    解释: 4没有超过3的两倍大, 所以我们返回 -1.


    提示:

    nums 的长度范围在[1, 50].
    每个 nums[i] 的整数范围在 [0, 99].
"""


class Solution(object):
    def dominantIndex(self, nums):
        """TODO：边界条件，一定存在一个最大值，则最大和次大不能相同
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:return None
        if len(nums)==1:return 0
        mx,mxi,m2x =max(nums),0,-999999
        for i,num in enumerate(nums):
            if num==mx:
                mxi=i
            elif num>m2x:
                m2x=num
        if mx>=m2x*2:
            return mxi
        else:
            return -1



if __name__ == '__main__':
    nums = [3, 6, 1, 0]
    nums = [1,0]
    solu =Solution()
    print(solu.dominantIndex(nums))

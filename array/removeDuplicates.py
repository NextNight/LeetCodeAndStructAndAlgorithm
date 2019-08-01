#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Date    : 2019-07-31
  @Author  : Kaka
  @File    : removeDuplicates.py
  @Software: PyCharm
  @Contact : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
  @Desc    : 删除排序数组中的重复项
  给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

    示例 1:

    给定数组 nums = [1,1,2],

    函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

    你不需要考虑数组中超出新长度后面的元素。
    示例 2:

    给定 nums = [0,0,1,1,1,2,2,3,3,4],

    函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

    你不需要考虑数组中超出新长度后面的元素。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        '''双指针覆盖删除法：原地算法
        '''
        if nums is None or len(nums) == 1:return 1
        p, r = 0, 1
        while r <= len(nums) - 1:
            # if nums[p] == nums[r]:
            #     r += 1
            # else:
            #     p += 1
            #     nums[p] = nums[r]
            #     r += 1

            if nums[p]!=nums[r]:
                p+=1
                nums[p] = nums[r]
            r+=1
        return p+1


if __name__ == '__main__':
    solu = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    p = solu.removeDuplicates(nums)
    print(p,nums[:p])
    assert nums[:5]==[0,1,2,3,4]

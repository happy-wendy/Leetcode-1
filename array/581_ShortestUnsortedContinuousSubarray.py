#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
先将数组排序赋给一个新的数组，通过两个数组之间的比较，第一个和最后一个元素不同的位置索引即为子数组的界限。
数组总长度减去正序的一个为False的位置和逆序第一个为False的位置
"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        sort_nums = sorted(nums)
        is_same = [a == b for a, b in zip(nums, sort_nums)]
        if all(is_same):
            return 0
        else:
            return len(nums) - is_same.index(False) - is_same[::-1].index(False)
            
"""
思路同上但写法不一样
"""
class Solution:
    def findUnsortedSubarray(self, nums):
        head = 0
        tail = len(nums)
        list2 = sorted(nums)
        for i,j in enumerate(nums):
            if j != list2[i]:
                head = i
                break
        for i,j in enumerate(nums[::-1]):
            if j != list2[::-1][i]:
                tail = i
                break
        return len(nums) - tail - head

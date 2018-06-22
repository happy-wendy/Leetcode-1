#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = set(nums)
        new = set(range(1, len(nums) + 1))
        return list(new - n)
        
"""
法一是集合，法二用正负号标记法（虽然都是正数，但没加abs会出错，为什么？）
"""
class Solution:
    def findDisappearedNumbers(self, nums):
        for n in nums:
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        return [i + 1 for i, n in enumerate(nums) if n > 0]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0
        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1
        for j in range(k, len(nums)):
            nums[j] = 0
            
"""
法二：map sort
"""
class Solution(object):
    def moveZeroes(self, nums):    
        nums.sort(key = lambda x: 1 if x == 0 else 0)

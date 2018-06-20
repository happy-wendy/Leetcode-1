#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
法一：局部最优和全局最优
-2 , 1, −3,4,−1,2,1,−5,4 
位置0，L=x=-2，没得选 
位置1，要以x=1为结尾的最大的，那肯定不要带上之前的-2,只要1就好L=x=1 
位置2，因为本身x=-3，加上上一个位置L 是正数1，所以L=L+x=-3+1=-2。
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        g = nums[0]
        l = 0
        for n in nums:
            l = max(n, n+l)
            g = max(l, g)
        return g

"""
法二：负数清0

"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cur_sum = 0
        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum

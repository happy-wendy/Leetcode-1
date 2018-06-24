#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for i in nums:
            if i in map:
                return True
            map[i] = True
        return False
   """
   或者这种字典写法，我的思路
   """
    if len(nums) <=1 :
            return False
        temp = dict()
        for num in nums:
            if temp.has_key(num):
                temp[num] += 1
                if temp[num] >=2:
                    return True
            else:
                temp[num] = 1
        return False
"""
法一通过字典，法二可先排序，法三直接利用集合长度
"""
nums.sort()
        for i in xrange(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
"""
法三
"""
return len(nums) != len(set(nums))

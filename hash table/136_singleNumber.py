#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1.Iterate through all elements in \text{nums}nums
2.Try if hash\_tablehash_table has the key for pop
3.If not, set up key/value pair
4.In the end, there is only one element in hash\_tablehash_table, so use popitem to get it
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
"""
异或操作的定义为：x ^ 0 = x; x ^ x = 0。用在这道题里面就是：y ^ x ^ x = y; x ^ x = 0
"""
class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for i in nums:
            res ^= i
        return res
        
"""
法二：都是用异或，但是更精简
reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，
reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
"""
return reduce(lambda x, y: x^y, nums)
return reduce(operator.xor, nums)

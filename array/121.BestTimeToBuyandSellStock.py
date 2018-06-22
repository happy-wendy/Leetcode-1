#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        dp = [0] * len(prices)
        for i in range(0, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return dp[-1]
        
"""
法二：一般解法
"""
class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            maxProfit = max(maxProfit, p - minPrice)             
        return maxProfit

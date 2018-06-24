#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        alpha = [0] * 26
        beta = [0] * 26
        for c in s:
            alpha[ord(c) - 97] += 1
        for c in t:
            beta[ord(c) - 97] += 1
        return alpha == beta
"""
法二 用字典（我写的有点不同）
法三 return sorted(s) == sorted(t)
"""
        if len(s) != len(t):
            return False

        alpha = {}
        beta = {}
        for c in s:
            alpha[c] = alpha.get(c, 0) + 1
        for c in t:
            beta[c] = beta.get(c, 0) + 1
        return alpha == beta
        
      

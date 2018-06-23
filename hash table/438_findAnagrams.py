#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        ls, lp = len(s), len(p)
        count  = lp
        cp = collections.Counter(p)
        for i in range(ls):
            if cp[s[i]] >= 1:
                count -= 1
            cp[s[i]] -= 1
            if i >= lp:
                if cp[s[i-lp]] >= 0:
                    count += 1
                cp[s[i-lp]] += 1
            if count == 0:
                ans.append(i - lp + 1)
        return ans
        
        """
        滑动窗口：
        首先统计字符串p的字符个数，然后用两个变量left和right表示滑动窗口的左右边界，用变量cnt表示字符串p中需要匹配的字符个数，然后开始循环，
        如果右边界的字符已经在哈希表中了，说明该字符在p中有出现，则cnt自减1，然后哈希表中该字符个数自减1，右边界自加1，如果此时cnt减为0了，
        说明p中的字符都匹配上了，那么将此时左边界加入结果res中。如果此时right和left的差为p的长度，说明此时应该去掉最左边的一个字符，
        我们看如果该字符在哈希表中的个数大于等于0，说明该字符是p中的字符，为啥呢，因为上面我们有让每个字符自减1，
        如果不是p中的字符，那么在哈希表中个数应该为0，自减1后就为-1，所以这样就知道该字符是否属于p，如果我们去掉了属于p的一个字符，cnt自增1
        """
        d = defaultdict(int)
	ns, np = len(s), len(p)
	ans = []
	
	for c in p:	d[c] -= 1
	
	for i in xrange(ns):
		if i < np:
			d[s[i]] += 1
			if not d[s[i]]: del d[s[i]]
			
		else:
			if not d: ans.append(i-np)
			
			d[s[i-np]] -= 1
			if not d[s[i-np]] : del d[s[i-np]]
			
			d[s[i]] += 1
			if not d[s[i]]: del d[s[i]]
	if not d: ans.append(i-np+1)
	
	return ans
        

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
直到两个长度相等时再比较
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        elif lenA < lenB:
            for i in range(lenB - lenA):
                headB = headB.next
        while headA != headB:
            headA, headB = headA.next, headB.next
        return headA

    def getListLen(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
        
        """
        定义两个指针，让它们都将两个链表都遍历一遍，那么它们走的总长度是一样的，倘若两个链表相交，那么这两个指针一定会在某个地方相等。
        """
        if not headA or not headB:
            return None
        p, q = headA, headB
        while p and q and p != q:
            p = p.next
            q = q.next
            if p == q:
                return p
            if not p:
                p = headB #A遍历完了就转到B
            if not q:
                q = headA
        return p

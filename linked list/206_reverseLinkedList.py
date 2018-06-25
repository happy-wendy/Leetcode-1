#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迭代：
通过迭代将节点重组，前面的节点转移到重组链表的后面
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head
        
"""
递归
"""
        if not head or not head.next: #
            return head

        p = head.next
        n = self.reverseList(p)

        head.next = None  #
        p.next = head
        return n

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
顺序遍历链表所有节点，若出现重复访问则说明有环，否则说明无环。
这里注意不能用list保存访问过的节点，查找太慢了；
用dict保存还要考虑到键不能是对象，所以这里采取以对象的id作为键的做法
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        map = {}
        while head:
            if id(head) in map:
                return True
            else:
                map[id(head)] = True
            head = head.next
        return False
"""
快慢指针法。定义两个指针：快指针每次走一步；慢指针每次走两步。依次循环下去，如果链表存在环，那么快慢指针一定会有相等的时候。
"""
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

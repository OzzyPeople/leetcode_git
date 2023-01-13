'''
https://leetcode.com/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example #1
# Input: head = 1 -> 2 -> 3 -> 4 -> 5
# Output: 5 -> 4 -> 3 -> 2 -> 1

# Example #2
# Input: head = 1 -> 2
# Output: 2 -> 1
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time -  n
# memory - n
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        f = []
        while head:  # while linked list is not empty
            f.append(head.val)  # take the current val
            head = head.next  # change the current val to the next

        newHead = ListNode()
        newTail = newHead
        for i in reversed(f):
            newTail.next = ListNode(i)
            newTail = newTail.next
        return newHead.next


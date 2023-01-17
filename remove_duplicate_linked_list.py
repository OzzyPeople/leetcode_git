from typing import Optional

#remove duplicates from unsorted linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time -  n
# memory - n
class Solution(object):
    def delete_duplicate(self, node):
        list_val = []
        while node:
            val = node.val
            if val in list_val:
                node = node.next
            else:
                list_val.append(val)
                node = node.next
        return list_val

'''
result = ListNode(5)
result.next = ListNode(4)
result.next.next  = ListNode(5)
result.next.next.next = ListNode(2)
result.next.next.next.next = ListNode(2)
a = Solution()
a.delete_duplicate(result)
'''
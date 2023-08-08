from typing import Optional
'''
https://leetcode.com/problems/add-two-numbers/
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add = 0 #for keeping  in mind 1
        dummy = out = ListNode()

        #add because if we have 1 in add but the l2 or l1 is None, we need to add it to the end
        while l1 or l2 or add:
            #if length of lists are different [1, 2,3] [2, 3,3,3,3]
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            ## new digit
            val = a + b + add
            #if 15
            add = val//10
            val = val%10 #остаток всегда одинаковый 15/10 and 5/10
            out.next = ListNode(val)

            #update
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            out = out.next

        return dummy.next

### help functions

#convert list to ListNode
def fill_list (l):
    cur = dummy = ListNode(0)
    for e in l:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next

def print_list(node):
    l = []
    while node:
        l.append(node.val)
        node = node.next
    print (l)

l1 = [2,4,3]
l2 = [5,6,4]
g1 = fill_list (l1)
g2 = fill_list (l1)

a = Solution()
b = a.addTwoNumbers(g1, g2)
print_list(b)
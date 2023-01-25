
'''
https://leetcode.com/problems/middle-of-the-linked-list/
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def findMiddle(self, head):
        l = []
        while head:
            l.append(head.val)
            head = head.next
        dl = len(l)
        if dl % 2 == 0:
            return int(dl / 2)+1
        else:
            return int(dl // 2)+1


    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        middle = self.findMiddle(head)
        count = 0
        #print_list(head)
        while head:
            count+=1
            if middle == count:
                return head
            head = head.next


def print_list(node):
    l = []
    while node:
        l.append(node.val)
        node = node.next
    print (l)


result = ListNode(1)
result.next = ListNode(2)
result.next.next  = ListNode(3)
result.next.next.next = ListNode(4)
result.next.next.next.next = ListNode(5)
a = Solution()
#print_list(result)
#print(a.findMiddle(result))
#print_list(a.traverse(result))

print_list(a.middleNode(result))

def traverse1(head):
    if head:
        print(head.val)
        traverse1(head.next)

'''
finding - linked list is like pack of sausages, if you cut, you have only the rest
'''


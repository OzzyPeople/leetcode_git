
'''
https://leetcode.com/problems/middle-of-the-linked-list/
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
'''

#memory - c
#speed - n

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def findMiddle(self, head):
        l = 0 #better counter
        while head:
            l+=1
            head = head.next
        if l % 2 == 0:
            return int(l / 2)+1
        else:
            return int(l // 2)+1


    def middleNode_1(self, head):
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

    #the idea is that fast list is 2 times faster, hense slow is middle
    def middleNode_2(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def middleNode_3(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]


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

print_list(a.middleNode_2(result))

def traverse1(head):
    if head:
        print(head.val)
        traverse1(head.next)

'''
finding - linked list is like pack of sausages, if you cut, you have only the rest
insted of len list is better to use counter
'''


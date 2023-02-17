class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time -  n
# memory - n
class Solution:
    def removeNthFromEnd_opt_1(self, head, n):

        dummy = ListNode(next=head) #чтобы было нулевое предыдущее значение
        prev, curr = dummy, head
        count = 0

        #считаем, сколько узлов в списке
        while curr:
            count += 1
            curr = curr.next
        #вычисляем позицию
        pos = count - n + 1
        count = 0

        curr = head
        while curr:
            count += 1
            if pos == count: #когда номер позиции совпадает, перескакиваем
                prev.next = curr.next
            else:
                prev = curr #если нет, двигаем список предыдущий на уровень curr
            curr = curr.next
        return dummy.next #in fact it is prev

#option 2
    def removeNthFromEnd_opt_2(self, head, n):
        start = ListNode()
        start.next = head
        fast = start
        slow = start

        for i in range(1, n + 1):
            fast = fast.next

        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return start.next

def print_list(node):
    l = []
    while node:
        l.append(node.val)
        node = node.next
    print (l)

result = ListNode(1)
result.next = ListNode(2)
#result.next.next  = ListNode(3)
#result.next.next.next = ListNode(4)
#result.next.next.next.next = ListNode(2)
a = Solution()
print_list(result)
nodes_0 = a.removeNthFromEnd_opt_1(result, 1)
nodes_1 = a.removeNthFromEnd_opt_2(result, 1)
print_list(nodes_0)
print_list(nodes_1)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyQueue:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        node = ListNode(val) #create new node

        # if there is no tail head and tail = node
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node  # add to the end of queue (append) добавляем не значение, а узел
            self.tail = node  # объявляем последний элемент хвостом, чтобы не перетереть его в след добавлениях

    def pop(self):
        if self.isempty():
            raise 'Exception - no head'
        else:
            val = self.head.val #take the first val in the linled lit
            self.head = self.head.next #затираем текущий head на следующий
            if self.head is None:  # если удалили единственный элемент и остался хвост, то его тоже надо удалить
                self.tail = None
        return val

    def isempty(self):
        return self.head is None  # True or False

#how to print the queue
q = MyQueue()
q.append(1)
q.append(2)
q.append(3)

while not q.isempty():
    print (q.pop())
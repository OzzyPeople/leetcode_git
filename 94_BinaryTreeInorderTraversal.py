#https://leetcode.com/problems/binary-tree-inorder-traversal/
#Given the root of a binary tree, return the inorder traversal of its nodes' values.


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        l = []
        self.helper(root, l)
        return l
    def helper(self, curr,acc): #рекурсия с состоянием - аккумулятор
        #acc - список, который потом анонсируем
        if not curr:
            return
        else:
            self.helper(curr.left, acc)
            acc.append(curr.val)
            self.helper(curr.right, acc)

root = Node(1)
#root.left = Node(2)
root.right = Node(2)
root.right.left = Node(3)
#root.left.right = Node(5)

a = Solution()
print(a.inorderTraversal(root))
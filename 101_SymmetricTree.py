'''
https://leetcode.com/problems/symmetric-tree/
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

'''

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
idea - add to stack tuples and in cycle pop them out.  
first to understand main condition after the second level. True if:
left.left == right.right 
left.right == right.left
Note: don't forgete that we compare values. 
'''

class Solution:

    def isSymmetric(self, root) -> bool:
        if not root:
            return True

        stack = []
        if root:
            stack.append((root.left, root.right))

        while (len(stack) > 0):
            left, right = stack.pop()
            if not left and not right:
                continue
            if left and right and left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((right.left, left.right))
            else:
                return False

        return True

    #recursive way

    def isSymmetric_rec (self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True

        if left and right and left.val == right.val:
            return self.helper(left.left, right.right) and self.helper(right.left, left.right)
        return False
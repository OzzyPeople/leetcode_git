
'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced binary search tree.

Solution:

0 we create helper function
1 median is our root it divides the array into two parts - left and right subtree
2 in each subtree we have left and right element (l, r)
3 for each subtree we create recursion with basic basic condition - right can't be less than left
4


Time complexity - O(n)
Memory complexity - nLog(n) - because of tree height
'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(l, r):
            if l > r:
                return None
            median = (l + r) // 2
            root = TreeNode(nums[median])
            root.left = helper(l, median - 1)
            root.right = helper(median + 1, r)
            return root
        return helper(0, len(nums) - 1)

#without additional function

    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        # find middle index
        mid = (len(nums)) // 2

        # make the middle element the root
        root = TreeNode(nums[mid])

        # left subtree of root has all
        # values <arr[mid]
        root.left = self.sortedArrayToBST(nums[:mid]) #not effective for memory, always cut array

        # right subtree of root has all
        # values >arr[mid]
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

    def sortedArrayToBST(self, nums):
        root = TreeNode(float('-inf'))  # previous value of tree
        stack = []

        stack.append((root, 'right', 0, len(nums) - 1))  # "left" because we need to know where to assign
        while stack:
            parent, side, left_border, right_border = stack.pop()
            if left_border > right_border:
                continue
            median = (left_border + right_border) // 2
            node = TreeNode(nums[median])
            if side == 'left':
                parent.left = node
            else:
                parent.right = node
            stack.append((node, 'left', left_border, median - 1))  # analog to root.left = helper(l, median - 1)
            stack.append((node, 'right', median + 1, right_border))

        return root.right  # like linked list

    def sortedArrayToBST_short(self, nums):
        def helper(left_border, right_border, parent, side):
            if left_border > right_border:
                return None
            median = (left_border + right_border) // 2
            node = TreeNode(nums[median])
            if side == 'left':
                parent.left = node
            else:
                parent.right = node
            helper(left_border, median - 1, node, 'left')
            helper(median + 1, right_border, node, 'right')
            return parent

        return helper(0, len(nums) - 1, TreeNode(float('inf')), 'left').left

nums = [-10,-3,0,5,9]


def preOrder(node):
    if not node:
        return

    print (node.val)
    preOrder(node.left)
    preOrder(node.right)


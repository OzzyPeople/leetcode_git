'''
Сложность: o(n) + o(n)
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given the root of a binary tree, return its maximum depth.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            if left > right:
                return left + 1
            else:
                return right +1

    def maxDepth_short(self, root):
        if not root:
            return 0
        return max(self.maxDepth_short(root.left) + 1, self.maxDepth_short(root.right) + 1)

    def maxDepth_stack(self, root):
        maximum = 0

        s = []
        if root:
            s.append((root, 1))

        while (s):
            curr, level = s.pop()
            if not curr.left and not curr.right:
                maximum = max(level, maximum)

            if curr.left:
                s.append((curr.left, level + 1))

            if curr.right:
                s.append((curr.right, level + 1))

        return maximum



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.left.right = TreeNode(5)

a = Solution()
a.maxDepth(root)
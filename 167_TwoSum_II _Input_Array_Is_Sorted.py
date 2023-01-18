
'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target. You may assume that each input would have exactly one solution,
and you may not use the same element twice. You can return the answer in any order.
'''

# time -  n
# memory - 2n - > n

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #create dict
        d = {} # memory - n
        for i, k in enumerate(nums): # memory - n
            d[k] = i
        for j, k in enumerate(nums): # memory - n
            h = target - k
            if h in d:
                return [j+1, d[h]+1] #index should be + 1 due to condition

'''
a = Solution()
a.twoSum([2,7,11,15], 9)
'''

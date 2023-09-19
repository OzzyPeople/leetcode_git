
'''
https://leetcode.com/problems/sort-array-by-parity/
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Key idea - two pointers - one for changing numbers another for checking the length of list
'''

def sortArrayByParity(nums):
    i = 0 #for list length
    k = 0 # for numbers
    while i < len(nums):
        if nums[k]%2>0:
            a = nums.pop(k)
            nums.append(a)
        else:
            k += 1
        i += 1
    return nums

nums = [3,1,2,4]

sortArrayByParity(nums)
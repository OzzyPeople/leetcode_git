'''
https://leetcode.com/problems/build-array-from-permutation/

Given a zero-based permutation nums (0-indexed),
build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

'''


def buildArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    for i, num in enumerate(nums):
        nums[i] += n * (nums[num] % n)

    for i in range(n):
        nums[i] //= n

    return nums

nums = [0,2,1,5,3,4]
#[0,2,5,3,4,1] instead of [0,1,2,4,5,3]
buildArray(nums)
'''
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing
subsequence
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

idea:
each number has its subseq. The smallest subseq is at the last num.
We iterate from RIGHT to LEFT to collect sum of subseq for each value under binary condition.
Then we take max
How:
- two pointers of index - i - and j
- if nums[i] (curr value) < nums[j] (next value i +1),
- nums[i] < nums[j]  =>  we add 1 to subseq[j] and compare it to subseq [i]

'''
# space - c
# speed - O(n^2)
def lengthOfLIS(nums):
    lis = [1] * len(nums) #1 for each seq as default
    #from RIGHT to LEFT
    for i in range (len(nums) - 1, -1, -1): #start from the end, stop at -1m step -1
        #LEFT [i+1] to Right
        for j in range (i +1, len(nums)):
            if nums[i] < nums[j]:
                lis[i] = max(lis[i], 1 + lis[j])
    print (max(lis))

nums = [10,9,2,5,3,7,101,18]
lengthOfLIS(nums)


'''

https://leetcode.com/problems/top-k-frequent-elements

# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

'''

from collections import Counter

#option 1
class Solution1:
    def topKFrequent(self, nums, k: int):
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]= 1
        a = [(y, x) for x, y in d.items()]
        a.sort(reverse=True) #sort the list with less lost of speed
        return [x[1] for x in a[:k]]

#option 2
class Solution2:
    def topKFrequent(self, nums, k: int):
        a = [(y, x) for x, y in Counter(nums).items()]
        a.sort(reverse=True)
        return [x[1] for x in a[:k]]

#option 3
class Solution3:
    def topKFrequent(self, nums, k: int):
        return [x[1] for x in sorted([(y, x) for x, y in Counter(nums).items()])[-k:]]
'''
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B',
representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks.

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3


'''

def minimumRecolors(blocks, k):
    countB = 0
    maxCountB = 0

    for i, block in enumerate(blocks):
        if block == 'B':
            countB += 1
        if i >= k and blocks[i - k] == 'B':
            countB -= 1
        maxCountB = max(maxCountB, countB)

    return k - maxCountB

blocks = "WBBWWBBWBW"
k = 7
minimumRecolors(blocks, k)
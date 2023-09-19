'''
https://leetcode.com/problems/points-that-intersect-with-cars/
You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line.
For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and
endi is the ending point of the ith car.

Return the number of integer points on the line that are covered with any part of a car.
'''

#space - n
#speed  - n

def numberOfPoints(nums):

    # Step 1. sort list
    nums = sorted(nums) #nlog(n)
    new_list = [nums[0]]
    curr = 1

    # Step 2. merge intervals if any
    while curr != len(nums):
        if new_list[-1][1] < nums[curr][0]:
            new_list.append(nums[curr])
        else:
            new_list[-1] = (new_list[-1][0], max(nums[curr][1], new_list[-1][1]))
        curr += 1

    # Step 3. num_points = diff end and start point +1
    res = 0
    for i in range(len(new_list)):
        val = new_list[i][1] - new_list[i][0] + 1
        res += val
    return res

nums = [[3,6],[1,5],[4,7]]
numberOfPoints(nums)
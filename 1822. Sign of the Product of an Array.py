'''
1822. Sign of the Product of an Array
1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.

'''

#option 1
def arraySign(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 1
    for x in nums:
        res = res * x
    if res > 0:
        return 1
    elif res == 0:
        return 0
    else:
        return -1

#option 2
# this one is smarter than previous.

def arraySign(nums):
    sign = 1
    for num in nums:
        if num == 0:
            return 0
        if num < 0:
            sign = -sign
    return sign
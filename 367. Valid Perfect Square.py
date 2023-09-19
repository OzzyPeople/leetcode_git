'''
https://leetcode.com/problems/valid-perfect-square/

A perfect square is an integer that is the square of an integer.
In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

idea - binary search
check condition -  mid*mid = num or 4*4 = 16

'''


def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    left = 1
    right = num

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        if square < num:
            left = mid + 1
        elif square > num:
            right = mid - 1
        else:
            return True

    return False


num = 16
isPerfectSquare(num)

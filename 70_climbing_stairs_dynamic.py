#time - o(n)
#space complexity - n

'''
https://leetcode.com/problems/climbing-stairs/description/
climbing stars

'''


class Solution:
    #top down dynamic coding 
    def climbStairs1 (self, n: int) -> int:
        f = {}
        return self.helper(n, f)

    def helper(self, n: int, f) -> int:
        if n ==1:
            return 1
        elif n ==2:
            return 2
        if n not in f:
            f[n] = self.helper(n-1, f) + self.helper(n-2, f)
        return f[n]

    #bottom up dynamic coding
    def climbStairs2(self, n: int) -> int:
        f = {}
        for i in range(1, n+1):
            if i == 1:
                f[i]=1
            elif i ==2:
                f[i]=2
            else:
                f[i] = f[i-1] + f[i-2]
        return f[n]
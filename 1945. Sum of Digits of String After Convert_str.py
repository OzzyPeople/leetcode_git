'''
https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

You are given a string s consisting of lowercase English letters, and an integer k.
First, convert s into an integer by replacing each letter with its position in the alphabet
(i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26).
Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

'''

def getLucky(s, k):
    letters = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    d_let= {j:k for k, j in enumerate(letters, start =1)}

    origin = ''
    for i in s:
        origin = origin + str(d_let[i])

    i = 1 # if 0 the result is 0
    string_till = origin
    res = 0
    while i <=k:
        till_res = [int(x) for x in string_till]
        res = sum(till_res)
        string_till = str(res)
        i +=1
    return res

s = "iiii"
k = 1

getLucky(s, k)



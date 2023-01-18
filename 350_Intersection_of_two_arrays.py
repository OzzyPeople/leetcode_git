'''
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two integer arrays nums1 and nums2,
return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and
you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
'''

#option 1
import time

#memory 2n -> n
#time - n * m

def intersection_big(num1, num2):
    #define which list is bigger
    if len(num1) > len(num2):
        small = num2
        big = num1
    else:
        small = num1
        big = num2

    #count dictionary - value = key , items = index in list
    # a = [5, 2, 1, 1, 5]
    # d = {5: [0, 4], 2: [1], 1: [2, 3]}
    list_index = 0
    big_d = {}  # change for small
    for i in big:
        index = i #big.index(i) #track index of big list
        if index not in big_d:
            big_d[index] = list()
            big_d[index].append(list_index)
            list_index +=1
        else:
            big_d[index].append(list_index) #if there is more than one same value
            list_index +=1
    res = []
    for i in small:
        if i in big_d:
            if len(big_d[i]) > 0:
                res.append(i)
                big_d[i].pop()

    return res

'''
n = 100000
t0 = time.time()
for i in range(n): intersection_big(num1, num2)
t1 = time.time()
total_big = t1-t0
'''

#memory 2n -> n
#time - n + m

def intersection_small(num1, num2):
    # define which list is bigger
    if len(num1) > len(num2):
        small = num2
        big = num1
    else:
        small = num1
        big = num2

    # count dictionary - value = key , items = index in list
    # a = [5, 2, 1, 1, 5]
    # d = {5: [0, 4], 2: [1], 1: [2, 3]}
    list_index = 0
    small_d = {}  # change for small
    for i in small:
        index = i  # big.index(i) #track index of big list
        if index not in small_d:
            small_d[index] = list()
            small_d[index].append(list_index)
            list_index += 1
        else:
            small_d[index].append(list_index)  # if there is more than one same value
            list_index += 1

    res = []
    for i in big:
        if i in small_d:
            if len(small_d[i]) > 0:
                res.append(i)
                small_d[i].pop()

    return res

''' RESUME 

первое решение - цикл в цикле - большое О было n * m 
второе решение - создать словарь на основе большого списка - большое О  n + m 
третье решение - создать словарь на основе маленького списка

'''
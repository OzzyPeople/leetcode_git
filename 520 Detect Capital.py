'''
https://leetcode.com/problems/detect-capital/

We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".

'''


def detectCapitalUse(word):

    # we count all upper cases
    upper_sum = sum([1 for x in word if x.isupper()])

    # case #1 - when all lowercase - "new"
    if upper_sum == 0:
        return True

    # case #2 -  1 uppercase - "New":
    if upper_sum == 1:
        return word[0].isupper()

    # case #3 -  all uppercase - "NEW":
    upper = word.upper()
    for i in range(len(word)):
        if word[i] != upper[i]:
            return False
    return True
'''
1935. Maximum Number of Words You Can Type
There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.
Given a string text of words separated by a single space (no leading or trailing spaces)
and a string brokenLetters of all distinct letter keys that are broken,
return the number of words in text you can fully type using this keyboard.

'''

def canBeTypedWords(text, brokenLetters):

    words = text.lower().split()
    count = [0] * len(words)
    notl = list(brokenLetters)
    for i in notl:
        for k in range(len(words)):
            if i in words[k]:
                count[k] = 1
                continue
    print (len(words) - sum(count))
    return len(words) - sum(count)

text = "leet code"
brokenLetters = "e"
canBeTypedWords(text, brokenLetters)

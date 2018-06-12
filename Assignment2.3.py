'''
2.​ Problem Statement

Implement a function longestWord() that takes a list of words and returns the longest
one.
'''


def longestword(lst):
    try:
        length = [len(i) for i in lst]
        return lst[length.index(max(length))]
    except Exception as e:
        print(e)

lst = ['Hello World', 'How are you']
print(longestword(lst))

a = [1, 2, 3, 4, 6, 7, 99, 88, 999]
max = 0
for i in a:
    if i > max:
        max = i
print(max)

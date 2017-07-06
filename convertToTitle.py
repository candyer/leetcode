# Leetcode 168 -- Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/#/description

# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# For example:
# 1 -> A
# 2 -> B
# 3 -> C
# ...
# 26 -> Z
# 27 -> AA
# 28 -> AB 


def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    # solution 1
    res = ''
    while n > 0:
        res = chr(65 + (n - 1) % 26) + res
        n = (n - 1) / 26
    return res

    # solution 2
    res = []
    while n > 0:
        res.append(chr(65 + (n - 1) % 26))
        n = (n - 1) / 26
    return ''.join(reversed(res))

# print convertToTitle(1) #A
# print convertToTitle(26) #Z
# print convertToTitle(29) #AC
# print convertToTitle(100) #CV
# print convertToTitle(704) #AAB
# print convertToTitle(19684) #ACCB
# print convertToTitle(-52) #''
# print convertToTitle(205891132094649)#AKWXKZFQSJA


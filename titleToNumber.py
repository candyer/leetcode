# Leetcode 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/#/description

# Related to question Excel Sheet Column Title
# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 

def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    #solution 1
    n = len(s)
    if n == 0: return 0
    res = i = 0
    while i<n-1:
        res += (ord(s[i])-64)*(26**(n-i-1))
        i += 1
    res += (ord(s[i])-64)
    return res
    

    #solution 2 
    res = 0
    for c in s:
        res = res * 26 + (ord(c) - 64)
    return res

# print titleToNumber("ACCB") #19684

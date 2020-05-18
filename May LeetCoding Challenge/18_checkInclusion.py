# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3333/

# Permutation in String

# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
# In other words, one of the first string's permutations is the substring of the second string.

 
# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").


# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
 
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

from collections import Counter
from string import ascii_lowercase
def checkInclusion(s1: str, s2: str) -> bool:
    d1 = dict(zip(ascii_lowercase, [0]*26))
    d2 = dict(zip(ascii_lowercase, [0]*26))
    m, n = len(s1), len(s2)
    for c in s1:
        d1[c] += 1
    count = 0
    for i in range(n):
        d2[s2[i]] += 1
        count += 1
        if count > m:
            d2[s2[i - m]] -= 1
            count -= 1
        if count == m:
            if d1 == d2:
                return True
    return False


assert(checkInclusion("ab", "eidbaooo") == True)
assert(checkInclusion("ab", "eidboaoo") == False)




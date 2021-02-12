# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3636/

# Valid Anagram

# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


assert(isAnagram("anagram", "nagaram") == True)
assert(isAnagram("rat", "car") == False)
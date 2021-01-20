# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3609/


# Longest Palindromic Substring


# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Example 3:
# Input: s = "a"
# Output: "a"

# Example 4:
# Input: s = "ac"
# Output: "a"
 

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case)


def longestPalindrome(s: str) -> str:
    n = len(s)
    dp = [[True if i == j else False for j in range(n)] for i in range(n)]  
    res, max_lens = s[0], 0
    for r in range(1, n):
        for l in range(r - 1, -1, -1):
            if s[r] == s[l] and (r - l < 2 or dp[r - 1][l + 1]):
                dp[r][l] = True
                if r - l + 1 > len(res):
                    res = s[l : r + 1] 
                if max_lens < r - l + 1:
                    res = s[l: r + 1]
                    max_lens = r - l + 1
    return res

assert(longestPalindrome("babad") == 'bab')
assert(longestPalindrome("cbbd") == 'bb')
assert(longestPalindrome("a") == 'a')
assert(longestPalindrome("ac") == 'a')
assert(longestPalindrome("bdacadbddddddd") == 'bdacadb')



# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3544/

# Longest Substring with At Least K Repeating Characters

# Given a string s and an integer k, return the length of the longest substring of s such that 
# the frequency of each character in this substring is less(??? should be greater!!!) than or equal to k.

# Example 1:
# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

# Example 2:
# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 
# Constraints:
# 1 <= s.length <= 10^4
# s consists of only lowercase English letters.
# 1 <= k <= 10^5




###################################################################
# Brute Force TLE
# Time Complexity : O(n^2)
# Time Complexity : O(1)  (O(26))
from collections import Counter
def longestSubstring(s: str, k: int) -> int:
    res = 0
    n = len(s)
    for i in range(n):
        for j in range(i + k, n + 1):
            d = Counter(s[i:j])
            if min(d.values()) >= k:
                res = max(res, j - i)
    return res




###################################################################
def longestSubstring(s, k):
    for c in set(s):
        if s.count(c) < k:
            return max(longestSubstring(sub_s, k) for sub_s in s.split(c))
    return len(s)


assert(longestSubstring("aaabb", 3) == 3)
assert(longestSubstring("ababbc", 2) == 5)
assert(longestSubstring("abbcccdddd", 2) == 9)
assert(longestSubstring("a", 2) == 0)










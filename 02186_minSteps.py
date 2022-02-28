# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

# 2186. Minimum Number of Steps to Make Two Strings Anagram II

# You are given two strings s and t. In one step, you can append any character to either s or t.
# Return the minimum number of steps to make s and t anagrams of each other.
# An anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# Example 1:
# Input: s = "leetcode", t = "coats"
# Output: 7
# Explanation: 
# - In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcodeas".
# - In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coatsleede".
# "leetcodeas" and "coatsleede" are now anagrams of each other.
# We used a total of 2 + 5 = 7 steps.
# It can be shown that there is no way to make them anagrams of each other with less than 7 steps.

# Example 2:
# Input: s = "night", t = "thing"
# Output: 0
# Explanation: The given strings are already anagrams of each other. Thus, we do not need any further steps.


# Constraints:
# 1 <= s.length, t.length <= 2 * 10^5
# s and t consist of lowercase English letters.



from collections import Counter
from string import ascii_lowercase
def minSteps(s: str, t: str) -> int:
    ds = Counter(s)
    dt = Counter(t)
    count = 0
    for c in ascii_lowercase:
        count += abs(ds[c] - dt[c])
    return count

assert(minSteps("leetcode", "coats") == 7)
assert(minSteps("night", "thing") == 0)


#######################################################
def minSteps(s: str, t: str) -> int:
    tmp = [0] * 26
    for c in s:
        tmp[ord(c) - ord('a')] += 1
    for c in t:
        tmp[ord(c) - ord('a')] -= 1
    return sum([abs(i) for i in tmp])

assert(minSteps("leetcode", "coats") == 7)
assert(minSteps("night", "thing") == 0)








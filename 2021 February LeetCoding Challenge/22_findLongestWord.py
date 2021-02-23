# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3649/


# Longest Word in Dictionary through Deleting


# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting 
# some characters of the given string. If there are more than one possible results, return the longest word with 
# the smallest lexicographical order. If there is no possible result, return the empty string.

# Example 1:
# Input:  s = "abpcplea", d = ["ale","apple","monkey","plea"]
# Output: "apple"

# Example 2:
# Input:  s = "abpcplea", d = ["a","b","c"]
# Output: "a"


# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.


from typing import List
def is_substring(s, word):
    i, j, m, n = 0, 0, len(s), len(word)
    if n > m:
        return False
    while i < m and j < n:
        if s[i] == word[j]:
            j += 1
        i += 1
    return j == n

def findLongestWord(s: str, d: List[str]) -> str:
    res = ''
    d.sort(key=lambda x: (-len(x), x))
    for word in d:
        if is_substring(s, word):
            return word
    return res


assert(findLongestWord("abpcplea", ["ale","apple","abple","monkey","plea"]) == "abple")
assert(findLongestWord("abpcplea", ["ale","apple","monkey","plea"]) == "apple")
assert(findLongestWord("abpcplea", ["a","b","c"]) == "a")















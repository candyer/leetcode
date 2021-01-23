# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3597/


# Check If Two String Arrays are Equivalent


# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.


# Example 1:
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

# Example 2:
# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false

# Example 3:
# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true

# Constraints:
# 1 <= word1.length, word2.length <= 10^3
# 1 <= word1[i].length, word2[i].length <= 10^3
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
# word1[i] and word2[i] consist of lowercase letters.



from typing import List
def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
	return ''.join(word1) == ''.join(word2)

assert(arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) == True)
assert(arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) == False)
assert(arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) == True)



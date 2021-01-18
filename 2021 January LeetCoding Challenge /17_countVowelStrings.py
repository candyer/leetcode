# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3607/

# Count Sorted Vowel Strings


# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) 
# and are lexicographically sorted.

# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

# Example 1:
# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

# Example 2:
# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

# Example 3:
# Input: n = 33
# Output: 66045
 
# Constraints:
# 1 <= n <= 50


# start_chr| a   | e  | i  | o  |  u |
# ---------------------------------------------
#   1      | 1   | 1  | 1  | 1  |  1 | -> 5
#   2      | 5   | 4  | 3  | 2  |  1 | -> 15
#   3      | 15  | 10 | 6  | 3  |  1 | -> 35
#   4      | 35  | 20 | 10 | 4  |  1 | -> 70
#   5      | 70  | 35 | 15 | 5  |  1 | -> 126
#   ...
# ---------------------------------------------

def countVowelStrings(n: int) -> int:
    arr = [1] * 5
    for i in range(n - 1):
        for j in range(3, -1, -1):
        	arr[j] += arr[j + 1]
    return sum(arr)


assert(countVowelStrings(1) == 5)
assert(countVowelStrings(2) == 15)
assert(countVowelStrings(3) == 35)
assert(countVowelStrings(33) == 66045)
assert(countVowelStrings(100) == 4598126)
        










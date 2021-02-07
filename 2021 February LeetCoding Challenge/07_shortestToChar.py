# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3631/

# Shortest Distance to a Character

# Given a string s and a character c that occurs in s, 
# return an array of integers answer where answer.length == s.length 
# and answer[i] is the shortest distance from s[i] to the character c in s.


# Example 1:
# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]

# Example 2:
# Input: s = "aaab", c = "b"
# Output: [3,2,1,0]
 

# Constraints:
# 1 <= s.length <= 10^4
# s[i] and c are lowercase English letters.
# c occurs at least once in s.



from typing import List
def shortestToChar(s: str, c: str) -> List[int]:
    n, indexes = len(s), [float('-inf')]
    for i in range(n):
        if s[i] == c:
            indexes.append(i)
    indexes.append(float('inf'))
    answer = [0] * n
    for j in range(1, len(indexes)):
        left, right = indexes[j - 1], indexes[j]
        for k in range(max(0, left + 1), min(right, n)):
            answer[k] = min(k - left, right - k)
    return answer


assert(shortestToChar("loveleetcode", c = "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])
assert(shortestToChar("aaab", c = "b") == [3, 2, 1, 0])



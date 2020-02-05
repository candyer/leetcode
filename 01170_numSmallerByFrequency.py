# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/description/


# 1170. Compare Strings by Frequency of the Smallest Character


# Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. 
# For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

# Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words 
# such that f(queries[i]) < f(W), where W is a word in words.

 
# Example 1:
# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

# Example 2:
# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
 

# Constraints:
# 1 <= queries.length <= 2000
# 1 <= words.length <= 2000
# 1 <= queries[i].length, words[i].length <= 10
# queries[i][j], words[i][j] are English lowercase letters.



from typing import List
from bisect import bisect

def f(s):
	return s.count(min(s))

def numSmallerByFrequency(queries: List[str], words: List[str]) -> List[int]:
	a = [f(query) for query in queries]
	b = [f(word) for word in words]
	b.sort()
	n1, n2 = len(a), len(b)
	answer = []
	for i in range(n1):
		tmp = n2 - bisect(b, a[i])
		answer.append(tmp)
	return answer

assert(numSmallerByFrequency(["cbd"], ["zaaaz"]) == [1])
assert(numSmallerByFrequency(["bbb","cc"], ["a","aa","aaa","aaaa"]) == [1, 2])
assert(numSmallerByFrequency(["cbd", "kjhgf"], ["zaaaz", "a"]) == [1, 1])



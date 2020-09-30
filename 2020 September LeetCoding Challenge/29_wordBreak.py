# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/558/week-5-september-29th-september-30th/3477/

# Word Break


# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

#################################################################
from typing import List
def wordBreak(s: str, wordDict: List[str]) -> bool:
  n = len(s)
  dp = [True] + [False] * n
  for right in range(1, n + 1):
      for left in range(right):
          if dp[left] and s[left:right] in wordDict:
              dp[right] = True
  return dp[-1]




#################################################################
from typing import List, Set, Dict
def can_break(s: str, memo: Dict[str, bool] , wordDict: Set[str]):
	if s in memo:
		return memo[s]
	if s in wordDict:
		memo[s] = True
		return True
	for i in range(1, len(s)):
		left = s[:i]
		right = s[i:]
		if right in wordDict and can_break(left, memo, wordDict):
			memo[s] = True
			return True
	memo[s] = False
	return False

def wordBreak(s: str, wordDict: List[str]) -> bool:
	return can_break(s, {}, set(wordDict))




#################################################################
from typing import List
from collections import deque
def wordBreak(s: str, wordDict: List[str]) -> bool:
	q = deque([s])
	seen = set() 
	while q:
		s = q.popleft()
		for word in wordDict:
			if s.startswith(word):
				remaining = s[len(word):]
				if remaining == "": 
					return True
				if remaining not in seen:
					q.append(remaining)
					seen.add(remaining)
	return False

assert(wordBreak("catscat", ["cat", "cats"]) == True)
assert(wordBreak("leetcode", ["leet", "code"]) == True)
assert(wordBreak("applepenapple", ["apple", "pen"]) == True)
assert(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False)


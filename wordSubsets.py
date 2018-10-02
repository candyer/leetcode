# https://leetcode.com/problems/word-subsets/description/

# 916. Word Subsets

# We are given two arrays A and B of words.  Each word is a string of lowercase letters.

# Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  
# For example, "wrr" is a subset of "warrior", but is not a subset of "world".

# Now say a word a from A is universal if for every b in B, b is a subset of a. 
# Return a list of all universal words in A.  You can return the words in any order.

 
# Example 1:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# Output: ["facebook","google","leetcode"]

# Example 2:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# Output: ["apple","google","leetcode"]

# Example 3:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# Output: ["facebook","google"]

# Example 4:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# Output: ["google","leetcode"]

# Example 5:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
# Output: ["facebook","leetcode"]
 

# Note:
# 1 <= A.length, B.length <= 10000
# 1 <= A[i].length, B[i].length <= 10
# A[i] and B[i] consist only of lowercase letters.
# All words in A[i] are unique: there isn't i != j with A[i] == A[j].

from collections import Counter, defaultdict
def wordSubsets(A, B):
	"""
	:type A: List[str]
	:type B: List[str]
	:rtype: List[str]
	"""
	b_dict = defaultdict(int)
	for b in B:
		for key, val in Counter(b).items():
			b_dict[key] = max(b_dict[key], val)

	res = []
	for a in A:
		a_dict = Counter(a)
		flag = True

		for key, val in b_dict.items():
			if a_dict[key] < val:
				flag = False
		if flag:
			res.append(a)
	return res
	

assert wordSubsets(["amazon","apple","facebook","google","leetcode"], ["x"]) == []
assert wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]) == ["facebook","google","leetcode"]
assert wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"]) == ["apple","google","leetcode"]
assert wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","oo"]) == ["facebook","google"]
assert wordSubsets(["amazon","apple","facebook","google","leetcode"], ["lo","eo"]) == ["google","leetcode"]
assert wordSubsets(["amazon","apple","facebook","google","leetcode"], ["ec","oc","ceo"]) == ["facebook","leetcode"]




# https://leetcode.com/problems/delete-columns-to-make-sorted/description/


# We are given an array A of N lowercase letter strings, all of the same length.
# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
# For example, if we have a string "abcdef" and deletion indices {0, 2, 3}, then the final string after deletion is "bef".
# Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.
# Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]]
# Return the minimum possible value of D.length.

 
# Example 1:
# Input: ["cba","daf","ghi"]
# Output: 1

# Example 2:
# Input: ["a","b"]
# Output: 0

# Example 3:
# Input: ["zyx","wvu","tsr"]
# Output: 3
 
# Note:
# 1 <= A.length <= 100
# 1 <= A[i].length <= 1000


def minDeletionSize(A):
	"""
	:type A: List[str]
	:rtype: int
	"""
	n = len(A)
	m = len(A[0])
	res = 0
	for i in range(m):
		tmp = '`'
		for j in range(n):
			if ord(A[j][i]) < ord(tmp):
				res += 1
				break
			else:
				tmp = A[j][i]
	return res


assert minDeletionSize(["cba","daf","ghi"]) == 1
assert minDeletionSize(["a","b"]) == 0
assert minDeletionSize(["zyx","wvu","tsr"]) == 3
assert minDeletionSize(["zxff","bccc"]) == 4





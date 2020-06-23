# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3366/

# Permutation Sequence

# The set [1,2,3,...,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"

# Given n and k, return the kth permutation sequence.

# Note:
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.

# Example 1:
# Input: n = 3, k = 3
# Output: "213"

# Example 2:
# Input: n = 4, k = 9
# Output: "2314"


from math import factorial
def getPermutation(n: int, k: int) -> str:
	nums = [str(i) for i in range(1, n + 1)]
	res, total, k = [], factorial(n), k - 1
	while nums:
		total //= n
		n -= 1
		pos =  k // total
		k %= total
		num = nums.pop(pos)
		res.append(num)	
	return ''.join(res)

assert(getPermutation(4, 9) == '2314')
assert(getPermutation(4, 21) == '4213')
assert(getPermutation(5, 12) == '13542')
assert(getPermutation(5, 75) == '41325')
assert(getPermutation(9, 299999) == '845697312')



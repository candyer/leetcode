# Arranging Coins

# You have a total of n coins that you want to form in a staircase shape,where every k-th row must have exactly k coins.
# Given n, find the total number of full staircase rows that can be formed.
# n is a non-negative integer and fits within the range of a 32-bit signed integer.

# Example 1:
# n = 5
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# Because the 3rd row is incomplete, we return 2.

# Example 2:
# n = 8
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# Because the 4th row is incomplete, we return 3.

###############################
# Brute force
# Time complexity: O(sqrt(n))
# Space complexity: O(1)
###############################
def arrangeCoins(n: int) -> int:
	i = 1
	while n >= i:
		n -= i
		i += 1
	return i - 1


###############################
# Binary search
# Time complexity: O(logn)
# Space complexity: O(1)
###############################
def arrangeCoins1(n: int) -> int:
	left, right = 1, n
	while left <= right:
		mid = (left + right) // 2
		curr_sum = sum_from_1_to_n(mid)
		if curr_sum == n:
			return mid
		elif curr_sum < n:
			left = mid + 1
		else:
			right = mid - 1
	return right

assert(arrangeCoins(6) == 3)
assert(arrangeCoins(8) == 3)
assert(arrangeCoins(16) == 5)

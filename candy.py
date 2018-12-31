# https://leetcode.com/problems/candy/description/


# 135. Candy


# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?


# Example 1:
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.



def candy(ratings):
	"""
	:type ratings: List[int]
	:rtype: int
	"""
	n = len(ratings)

	left_to_right = [1]
	for i in range(1, n):
		if ratings[i] > ratings[i - 1]:
			left_to_right.append(left_to_right[i - 1] + 1)
		else:
			left_to_right.append(1)

	right_to_left = [1] * n
	for i in range(n - 2, -1, -1):
		if ratings[i + 1] < ratings[i]:
			right_to_left[i] = right_to_left[i + 1] + 1
		else:
			right_to_left[i] = 1

	count = 0
	for a, b in zip(left_to_right, right_to_left):
		count += max(a, b)
	return count


assert candy([1,0,2]) == 5
assert candy([1,2,2]) == 4




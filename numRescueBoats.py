# https://leetcode.com/problems/boats-to-save-people/description/

# 885. Boats to Save People

# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)


# Example 1:
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)

# Example 2:
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)

# Example 3:
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)

# Note:
# 1 <= people.length <= 50000
# 1 <= people[i] <= limit <= 30000


def numRescueBoats(people, limit):
	"""
	:type people: List[int]
	:type limit: int
	:rtype: int
	"""
	n = len(people)
	people.sort()
	left, right = 0, n - 1
	count = 0
	while left <= right:
		if people[left] + people[right] <= limit:
			left += 1
		right -= 1
		count += 1
	return count


assert numRescueBoats([1,2], 3) == 1
assert numRescueBoats([3,2,2,1], 3) == 3
assert numRescueBoats([3,5,3,4], 5) == 4

# from random import randint as r
# people = []
# limit = r(1, 10)
# for i in range(10):
# 	people.append(r(1, limit))
# print people, limit
# print numRescueBoats(people, limit)



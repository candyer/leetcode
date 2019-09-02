# https://leetcode.com/problems/diet-plan-performance/description/


# 1176. Diet Plan Performance

# A dieter consumes calories[i] calories on the i-th day.  For every consecutive sequence of k days, 
# they look at T, the total calories consumed during that sequence of k days:

# If T < lower, they performed poorly on their diet and lose 1 point; 
# If T > upper, they performed well on their diet and gain 1 point;
# Otherwise, they performed normally and there is no change in points.
# Return the total number of points the dieter has after all calories.length days.

# Note that: The total points could be negative.


# Example 1:
# Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
# Output: 0
# Explaination: calories[0], calories[1] < lower and calories[3], calories[4] > upper, total points = 0.

# Example 2:
# Input: calories = [3,2], k = 2, lower = 0, upper = 1
# Output: 1
# Explaination: calories[0] + calories[1] > upper, total points = 1.

# Example 3:
# Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
# Output: 0
# Explaination: calories[0] + calories[1] > upper, calories[2] + calories[3] < lower, total points = 0.
 

# Constraints:
# 1 <= k <= calories.length <= 10^5
# 0 <= calories[i] <= 20000
# 0 <= lower <= upper


def dietPlanPerformance(calories, k, lower, upper):
	"""
	:type calories: List[int]
	:type k: int
	:type lower: int
	:type upper: int
	:rtype: int
	"""
	n = len(calories)
	tmp = sum(calories[:k])
	res = 0
	for i in range(k, n + 1):
		if tmp > upper:
			res += 1
		elif tmp < lower:
			res -= 1

		tmp -= calories[i - k]
		if i < n:
			tmp += calories[i]
	return res

assert dietPlanPerformance([1,2,3,4,5], 2, 3, 4) == 3
assert dietPlanPerformance([1,2,3,4,5], 1, 3, 3) == 0
assert dietPlanPerformance([3,2], 2, 0, 1) == 1
assert dietPlanPerformance([6,5,0,0], 2, 1, 5) == 0



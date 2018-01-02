
# https://leetcode.com/contest/weekly-contest-65/problems/reach-a-number/


# You are standing at position 0 on an infinite number line. There is a goal at position target.

# On each move, you can either go left or right. During the n-th move (starting from 1), 
# you take n steps.

# Return the minimum number of steps required to reach the destination.

# Example 1:     Input: target = 3       Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.

# Example 2:     Input: target = 2       Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.

# Note:
# target will be a non-zero integer in the range [-10^9, 10^9].


def reachNumber(target):
	"""
	:type target: int
	:rtype: int
	"""
	target = abs(target)
	step = 0
	while target > 0:
		step += 1
		target -= step
	if target % 2 == 0:
		return step
	while target % 2 != 0:
		step += 1
		target -= step
		if target % 2 == 0:
			return step 

print reachNumber(-1000) == 47
print reachNumber(46) == 11



# https://leetcode.com/problems/daily-temperatures/description/

# 739. Daily Temperatures

# Given a list of daily temperatures, produce a list that, for each day in the input, tells you 
# how many days you would have to wait until a warmer temperature. If there is no future day for 
# which this is possible, put 0 instead.

# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should 
# be [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an 
# integer in the range [30, 100].

##############################
###### brute force TLE #######
##############################

def dailyTemperatures(temperatures):
	"""
	:type temperatures: List[int]
	:rtype: List[int]
	"""
	res = []
	n = len(temperatures)
	i = 0
	while i < n:
		count = 0
		for j in xrange(i + 1, n):
			if temperatures[j] > temperatures[i]:
				count = j - i
				break
		res.append(count)
		i += 1
	return res


##############################
#######   stack AC     #######
##############################


def dailyTemperatures2(temperatures):
	"""
	:type temperatures: List[int]
	:rtype: List[int]
	"""
	n = len(temperatures)
	res = [0] * n
	stack = []
	for i in range(n - 1, -1 , -1):
		while stack and temperatures[i] >= temperatures[stack[-1]]:
			stack.pop()
		if stack:
			res[i] = stack[-1] - i
		stack.append(i)
	return res

assert dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert dailyTemperatures([1, 3, 2, 4, 4, 7]) == [1, 2, 1, 2, 1, 0]

# from random import randint as r
# array = []
# for _ in range(30000):
# 	array.append(r(30, 100))
# print dailyTemperatures(array)


# import cProfile
# cProfile.run('dailyTemperatures(array)')
# cProfile.run('dailyTemperatures2(array)')






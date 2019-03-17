# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/


# 1013. Pairs of Songs With Total Durations Divisible by 60


# In a list of songs, the i-th song has a duration of time[i] seconds. 

# Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  
# Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

 
# Example 1:
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

# Example 2:
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 
# Note:
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500

from collections import Counter
def numPairsDivisibleBy60(time):
	"""
	:type time: List[int]
	:rtype: int
	"""
	d = Counter(time)
	times = d.keys()
	n = len(d)
	res = 0
	for i in range(n):
		for j in range(i + 1, n):
			if (times[i] + times[j]) % 60 == 0:
				res += d[times[i]] * d[times[j]]
	for t in times:
		if d[t] > 1 and t * 2 % 60 == 0:
			res += d[t] * (d[t] - 1) / 2
	return res




assert numPairsDivisibleBy60([30,20,150,100,40, 20, 20, 20, 20]) == 11
assert numPairsDivisibleBy60([60,60,60]) == 3
assert numPairsDivisibleBy60([30, 30, 30, 30, 60]) == 6
assert numPairsDivisibleBy60([60]) == 0
assert numPairsDivisibleBy60([70]) == 0



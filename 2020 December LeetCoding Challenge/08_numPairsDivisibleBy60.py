# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3559/

# Pairs of Songs With Total Durations Divisible by 60


# You are given a list of songs where the ith song has a duration of time[i] seconds.
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. 
# Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 
# Example 1:
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

# Example 2:
# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

# Constraints:
# 1 <= time.length <= 6 * 10^4
# 1 <= time[i] <= 500

from typing import List
from collections import defaultdict
def numPairsDivisibleBy60(time: List[int]) -> int:
	d = defaultdict(int)
	for duration in time:
		d[duration % 60] += 1
	res = 0
	for k, v in d.items():
		if k in [0, 30]:
			res += v * (v - 1) // 2
		elif k < 30 and 60 - k in d:
			res += d[k] * d[60 - k]
	return res

assert(numPairsDivisibleBy60([30,20,150,100,40]) == 3)
assert(numPairsDivisibleBy60([60,60,60]) == 3)
assert(numPairsDivisibleBy60([1, 1, 1, 59, 3, 5, 24, 36]) == 4)
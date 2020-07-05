# https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3380/

# Ugly Number II

# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime prime_factors only include 2, 3, 5. 

# Example:
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

# Note:  
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# import math

############ Brute Force TLE ############
def is_ugly_number(num):
	for divisor in [2, 3, 5]:
		while num % divisor == 0:
			num /= divisor
	return num == 1

def nthUglyNumber(n: int) -> int:
	if n == 1: return 1
	num = count = 1 
	while count < n:
		num += 1
		if is_ugly_number(num):
			count += 1	
	return num



############ DP AC ####################
# Time complexity: O(N)
# space complexity: O(N)
def nthUglyNumber(n: int) -> int:
	ugly_number = [1]
	i2 = i3 = i5 = 0
	for i in range(1, n):
		next_ugly_number = min(ugly_number[i2] * 2, ugly_number[i3] * 3, ugly_number[i5] * 5)
		ugly_number.append(next_ugly_number)
		if next_ugly_number == ugly_number[i2] * 2:
			i2 += 1
		if next_ugly_number == ugly_number[i3] * 3:
			i3 += 1
		if next_ugly_number == ugly_number[i5] * 5:
			i5 += 1
	return ugly_number[-1]


assert(nthUglyNumber(10) == 12)
assert(nthUglyNumber(32) == 90)
assert(nthUglyNumber(1600) == 1399680000)
assert(nthUglyNumber(1689) == 2109375000)


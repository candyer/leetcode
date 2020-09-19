# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3465/

# Sequential Digits

# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]

# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
 
# Constraints:
# 10 <= low <= high <= 10^9


#################################################################
from typing import List
def generate_all_sequential_digits():
	nums = []
	start = gap = 1
	for i in range(2, 10):
		num = start * 10 + i 
		gap = gap * 10 + 1
		for j in range(10 - i, 0, -1):
			nums.append(num)
			num += gap
		start = start * 10 + i
	return nums

def sequentialDigits(low: int, high: int) -> List[int]:
	res = []
	for num in generate_all_sequential_digits():
		if low <= num <= high:
			res.append(num)
	return res


	
#################################################################
def sequentialDigits(low: int, high: int) -> List[int]:
	res = []
	for i in range(1, 10):
		num = nexts = i
		while num <= high and nexts < 10:
			if num >= low:
				res.append(num)
			nexts += 1
			num = num * 10 + nexts
	return sorted(res)



assert(sequentialDigits(100, 300) == [123, 234])
assert(sequentialDigits(1000, 13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345])
assert(sequentialDigits(14, 543) == [23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456])












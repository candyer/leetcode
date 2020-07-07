# https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3382/

# Plus One
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, 
# and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


from typing import List
def plusOne(digits: List[int]) -> List[int]:
	i = len(digits) - 1
	while digits[i] == 9:
		digits[i] = 0
		i -= 1
	if i == -1:
		return [1] + digits
	else:
		digits[i] += 1
		return digits

def plusOne(digits, carry = 1):
	res = []
	for digit in digits[::-1]:
		val = digit + carry
		carry = val // 10
		res.append(val % 10)
	while carry:
		res.append(carry % 10)
		carry //= 10
	return res[::-1]


assert(plusOne([1,2,3]) == [1, 2, 4])
assert(plusOne([4,3,2,1]) == [4, 3, 2, 2])
assert(plusOne([9,9,9]) == [1, 0, 0, 0])
assert(plusOne([2,3,1,9]) == [2, 3, 2, 0])
assert(plusOne([0]) == [1])





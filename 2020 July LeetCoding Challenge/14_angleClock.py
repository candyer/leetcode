# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3390/

 # Angle Between Hands of a Clock

# Given two numbers, hour and minutes. Return the smaller angle (in degrees)
# formed between the hour and the minute hand.

# Example 1:
# Input: hour = 12, minutes = 30
# Output: 165

# Example 2:
# Input: hour = 3, minutes = 30
# Output: 75

# Example 3:
# Input: hour = 3, minutes = 15
# Output: 7.5

# Example 4:
# Input: hour = 4, minutes = 50
# Output: 155

# Example 5:
# Input: hour = 12, minutes = 0
# Output: 0

# Constraints:
# 1 <= hour <= 12
# 0 <= minutes <= 59
# Answers within 10^-5 of the actual value will be accepted as correct.


def angleClock(hour: int, minutes: int) -> float:
	m = minutes / 5
	h = hour % 12 + minutes / 60
	angle = abs(m - h) * 30
	return min(angle, 360 - angle)

assert(angleClock(12, 30) == 165.0)
assert(angleClock(3, 30) == 75.0)
assert(angleClock(3, 15) == 7.5)
assert(angleClock(4, 50) == 155.0)
assert(angleClock(11, 0) == 30.0)
assert(angleClock(2, 43) == 176.5)
assert(angleClock(8, 30) == 75.0)

# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3412/

# Power of Four

# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:
# Input: 16
# Output: true

# Example 2:
# Input: 5
# Output: false
# Follow up: Could you solve it without loops/recursion?

def isPowerOfFour(num: int) -> bool:
	if num <= 0: return False
	while num > 1:
		if num % 4 != 0:
			return False
		num //= 4
	return True



def isPowerOfFour(num):
	'''
	n,  pow(n, 4),    bin(pow(n, 4)),           len(bin(pow(n, 4)))
	1   4              0b100                              5
	2   16             0b10000                            7
	3   64             0b1000000                          9
	4   256            0b100000000                        11
	5   1024           0b10000000000                      13
	6   4096           0b1000000000000                    15
	7   16384          0b100000000000000                  17
	8   65536          0b10000000000000000                19
	9   262144         0b1000000000000000000              21
	10  1048576        0b100000000000000000000            23
	11  4194304        0b10000000000000000000000          25
	12  16777216       0b1000000000000000000000000        27
	13  67108864       0b100000000000000000000000000      29
	14  268435456      0b10000000000000000000000000000    31
	15  1073741824     0b1000000000000000000000000000000  33
	'''
	return num != 0 and num & (num - 1) == 0 and len(bin(num)) % 2 == 1


assert(isPowerOfFour(1) == True)
assert(isPowerOfFour(16) == True)
assert(isPowerOfFour(256) == True)
assert((isPowerOfFour(8) == False))
assert(isPowerOfFour(0) == False)
assert(isPowerOfFour(268) == False)
assert(isPowerOfFour(0) == False)
assert(isPowerOfFour(5) == False)
assert(isPowerOfFour(81) == False)


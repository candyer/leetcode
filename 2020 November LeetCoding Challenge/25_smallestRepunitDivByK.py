# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3543/

# Smallest Integer Divisible by K


# Given a positive integer K, you need to find the length of the smallest positive integer N such that
#  N is divisible by K, and N only contains the digit 1.

# Return the length of N. If there is no such N, return -1.

# Note: N may not fit in a 64-bit signed integer.

# Example 1:
# Input: K = 1
# Output: 1
# Explanation: The smallest answer is N = 1, which has length 1.

# Example 2:
# Input: K = 2
# Output: -1
# Explanation: There is no such positive integer N divisible by 2.

# Example 3:
# Input: K = 3
# Output: 3
# Explanation: The smallest answer is N = 111, which has length 3.
 

# Constraints:
# 1 <= K <= 10^5


def smallestRepunitDivByK(K: int) -> int:
    remainder = 0
    remainders = set()
    for i in range(K):
        remainder *= 10
        remainder += 1
        remainder %= K
        if remainder == 0:
            return i + 1
        else:
            if remainder not in remainders:
                remainders.add(remainder)
            else:
                return -1  

assert(smallestRepunitDivByK(1) == 1)
assert(smallestRepunitDivByK(2) == -1)
assert(smallestRepunitDivByK(3) == 3)
assert(smallestRepunitDivByK(4) == -1)
assert(smallestRepunitDivByK(5) == -1)
assert(smallestRepunitDivByK(7) == 6)
assert(smallestRepunitDivByK(1001) == 6)







# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3738/


# Count Primes

# Count the number of prime numbers less than a non-negative number, n.

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0
 
# Constraints:
# 0 <= n <= 5 * 10^6

def countPrimes(n: int) -> int:
    if n < 2: 
        return 0
    primes = [False, False] + [True] * (n - 2)
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i * i, n, i):
            primes[j] = False
    return sum(primes)

assert(countPrimes(29) == 9)
assert(countPrimes(10) == 4)
assert(countPrimes(0) == 0)
assert(countPrimes(1) == 0)
assert(countPrimes(2) == 0)


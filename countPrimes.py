# https://leetcode.com/problems/count-primes/description/

# 204. Count Primes

# Count the number of prime numbers less than a non-negative number, n.


def countPrimes(n):
	"""
	:type n: int
	:rtype: int
	"""
	if n <= 2:
		return 0
	res = [True] * n
	res[0] = res[1] = False
	for i in range(2, int(n ** 0.5) + 1):
		if res[i]:
			for j in range(i*2, n, i):
				res[j] = False
	return sum(res)

# import cProfile
# cProfile.run('countPrimes(1000000)')

assert countPrimes(2) == 0
assert countPrimes(100) == 25
assert countPrimes(999999) == 78498



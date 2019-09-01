# https://leetcode.com/problems/prime-arrangements/description/

# 1175. Prime Arrangements


# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

# (Recall that an integer is prime if and only if it is greater than 1, 
# and cannot be written as a product of two positive integers both smaller than it.)

# Since the answer may be large, return the answer modulo 10^9 + 7.


# Example 1:
# Input: n = 5
# Output: 12
# Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.

# Example 2:
# Input: n = 100
# Output: 682289015
 
# Constraints:
# 1 <= n <= 100


from math import factorial as f
def sieve(n):
	primes = []
	flag = [True] * n
	for i in range(2, n):
		if flag[i] == True:
			primes.append(i) 
		for j in range(i * i, n, i):
			flag[j] = False
	return primes	

def numPrimeArrangements(n):
	"""
	:type n: int
	:rtype: int
	"""
	mod = 10**9 + 7
	primes = sieve(n + 1)
	m = len(primes)
	return f(m) * f(n - m) % mod



assert numPrimeArrangements(5) == 12
assert numPrimeArrangements(7) == 144
assert numPrimeArrangements(11) == 86400
assert numPrimeArrangements(89) == 673469112
assert numPrimeArrangements(100) == 682289015




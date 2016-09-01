# Leetcode 70 -- Climbing Stairs

# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


#solution 1  toooo slow
import itertools
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    choices = []
    total = 0
    for nums_2 in range(n/2 + 1):
        nums_1 = n - nums_2*2
        choices = [1]*nums_1 + [2]*nums_2
        combinations = len(set(itertools.permutations(choices)))
        total += combinations
    return total


#solution 2  toooo slow  O(n**2)
def factorial(n):
    """ this function can be replaced by 'math.factorial(n)'  """
    total = 1
    while n > 0:
        total *= n
        n -= 1
    return total

def combinations(a,b):
    """ a>=b """
    assert a >= b, 'you cannot choose {} elements from {}'.format(a,b)
    return factorial(a) / (factorial(b) * factorial( a - b ))

# print combinations(10,3) #120
# print combinations(10,30) #AssertionError: you cannot choose 10 elements from 30

def climbStairs(n):
    total = 0
    for nums_2 in range(n/2 + 1):
        nums_1 = n - nums_2 * 2
        total += combinations(nums_1 + nums_2, nums_2)
    return total


#solution 3-1  brute force  O(2**n)
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1
    num = climbStairs(n - 1)
    if n >= 2:
        num += climbStairs(n - 2)
    return num


# solution 3-2   brute force  O(2**n)
def climbStairs(n, current=[]):
    """
    :type n: int
    :rtype: int
    """
    print 'working on size {} for path {}'.format(n, current)
    if n == 0:
        return [current]

    ways = climbStairs(n-1, current + [1])
    if n >= 2:
        ways += climbStairs(n-2, current + [2])
    return ways
# print climbStairs(5)


#solution 4-1 dynamic programming using memoization  O(n) running time, O(n) space
def memoize(f):
    memo = {}
    def helper(x,current=[]):
        if x not in memo:            
            memo[x] = f(x,current=[])
        return memo[x]
    return helper
    
@memoize
def climbStairs(n, current=[]):
    """
    :type n: int
    :rtype: int
    """
    # print 'working on size {} for path {}'.format(n, current)
    if n == 0:
        return 1
    num = climbStairs(n-1, current + [1])
    if n >= 2:
        num += climbStairs(n-2, current + [2])
    return num
# print climbStairs(100)


#solution 4-2 dynamic programming using memoization  O(n) running time, O(n) space
# dynamic programming by hand
def climbStairs(n):
    vals = [1, 1]
    for i in range(2, n + 1):
        vals.append(vals[i - 2] + vals[i - 1])
    return vals[n]
# print climbStairs(5)


#solution 5  dynamic programming O(n) running time, O(1) space
def climbStairs(n):
    minus_1, minus_2 = 1, 1
    for i in range(2, n + 1):
        minus_2, minus_1 = minus_1, minus_1 + minus_2
    return minus_1


#solution 6 using fibonacci closed form   O(log(n)) running time, O(1) space
def f(k):
    sqt = 5**0.5
    k = n + 1
    return int(((1 + sqt) ** k - (1 - sqt) ** k)/((2**k) * (sqt)))

print climbStairs(0) #1
print climbStairs(1) #1
print climbStairs(2) #2
print climbStairs(3) #3
print climbStairs(4) #5
print climbStairs(5) #8
print climbStairs(6) #13
print climbStairs(7) #21
print climbStairs(8) #34
print climbStairs(9) #55
print climbStairs(10) #89

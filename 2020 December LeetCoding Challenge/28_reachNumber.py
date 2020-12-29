# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3583/

# Reach a Number

# You are standing at position 0 on an infinite number line. There is a goal at position target.
# On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.
# Return the minimum number of steps required to reach the destination.


# Example 1:
# Input: target = 3
# Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.

# Example 2:
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.

# Note:
# target will be a non-zero integer in the range [-10^9, 10^9].



def reachNumber(target: int) -> int:
    if target < 0: target *= -1
    pos = step = 0
    while pos < target:
        step += 1
        pos += step
    diff = pos - target
    if diff % 2 == 0: #11 -> 1,-2,3,4,5
        return step 
    else:
        return step + 1 + step % 2 #12 -> 1,-2,3,4,5,-6,7



assert(reachNumber(3) == 2)
assert(reachNumber(2) == 3)
assert(reachNumber(6) == 3)

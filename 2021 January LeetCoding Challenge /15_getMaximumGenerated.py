# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3605/


# Get Maximum in Generated Array


# You are given an integer n. An array nums of length n + 1 is generated in the following way:

# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] when 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
# Return the maximum integer in the array nums​​​.

# Example 1:
# Input: n = 7
# Output: 3
# Explanation: According to the given rules:
#   nums[0] = 0
#   nums[1] = 1
#   nums[(1 * 2) = 2] = nums[1] = 1
#   nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
#   nums[(2 * 2) = 4] = nums[2] = 1
#   nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
#   nums[(3 * 2) = 6] = nums[3] = 2
#   nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
# Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.

# Example 2:
# Input: n = 2
# Output: 1
# Explanation: According to the given rules, the maximum between nums[0], nums[1], and nums[2] is 1.

# Example 3:
# Input: n = 3
# Output: 2
# Explanation: According to the given rules, the maximum between nums[0], nums[1], nums[2], and nums[3] is 2.
 

# Constraints:
# 0 <= n <= 100


def getMaximumGenerated(n: int) -> int:
    arr = [0, 1]
    if n <= 1:
        return arr[n]
    for i in range(2, n + 1):
        arr.append(arr[i // 2])
        if i % 2:
            arr[-1] += arr[i // 2 + 1]
    return max(arr)


def getMaximumGenerated(n: int) -> int:
    arr = [0, 1]
    if n <= 1:
        return arr[n]
    for i in range(1, n // 2 + 1):
        arr.append(arr[i])
        if i * 2 + 1 <= n:
            arr.append(arr[i] + arr[i + 1])
    return max(arr)

assert(getMaximumGenerated(7) == 3)
assert(getMaximumGenerated(2) == 1)
assert(getMaximumGenerated(3) == 2)
assert(getMaximumGenerated(0) == 0)
assert(getMaximumGenerated(1) == 1)
assert(getMaximumGenerated(20) == 7)
assert(getMaximumGenerated(93) == 21)




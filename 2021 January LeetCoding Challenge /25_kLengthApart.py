# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3616/

# Check If All 1's Are at Least Length K Places Away


# Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, 
# otherwise return False.

# Example 1:
# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.

# Example 2:
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.

# Example 3:
# Input: nums = [1,1,1,1,1], k = 0
# Output: true

# Example 4:
# Input: nums = [0,1,0,1], k = 1
# Output: true
 

# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= k <= nums.length
# nums[i] is 0 or 1


from typing import List
def kLengthApart(nums: List[int], k: int) -> bool:
    pre = -1
    for i in range(len(nums)):
        if nums[i]:
            if pre == -1:
                pre = i
            else:
                if i - pre - 1 < k:
                    return False
                pre = i
    return True

assert(kLengthApart([0,0,0,1,1,0], 2) == False)
assert(kLengthApart([1,0,0,0,1,0,0,1], 2) == True)
assert(kLengthApart([1,0,0,1,0,1], 2) == False)
assert(kLengthApart([1,1,1,1,1], 0) == True)
assert(kLengthApart([0,1,0,1], 1) == True)
assert(kLengthApart([1,0,0,0,1,0,0,0,1,0], 2) == True)
assert(kLengthApart([0,1,0,0], 2) == True)






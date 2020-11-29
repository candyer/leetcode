# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3546/

# Sliding Window Maximum


# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array 
# to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.


# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Example 3:
# Input: nums = [1,-1], k = 1
# Output: [1,-1]

# Example 4:
# Input: nums = [9,11], k = 2
# Output: [11]

# Example 5:
# Input: nums = [4,-2], k = 2
# Output: [4]
 

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length

########################################################################
from typing import List
from heapq import heappush, heappop
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    n, heap = len(nums), []
    for i in range(k):
        heappush(heap, (nums[i] * (-1), i))
    res, start, end = [], 0, k - 1
    while end < n:

        while True:
            maxi, pos = heappop(heap)
            if pos >= start:
                maxi *= (-1)
                break  

        res.append(maxi) 
        heappush(heap, (maxi * (-1), pos)) 
        start += 1
        end += 1
        if end < n:
            heappush(heap, (nums[end] * (-1), end))
    return res




assert(maxSlidingWindow([5, 4, 3, 2, 7], 3) == [5, 4, 7])
assert(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3, 3, 5, 5, 6, 7])
assert(maxSlidingWindow([7, 6, 3, 5, 1,3,-1,-3], 3) == [7, 6, 5, 5, 3, 3])
assert(maxSlidingWindow([1], 1) == [1])
assert(maxSlidingWindow([1,-1], 1) == [1, -1])
assert(maxSlidingWindow([9,11], 2) == [11])
assert(maxSlidingWindow([4,-2], 2) == [4])
assert(maxSlidingWindow([4], 1) == [4])






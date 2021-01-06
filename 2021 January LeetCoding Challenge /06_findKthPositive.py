# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3594/


# Kth Missing Positive Number


# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Find the kth positive integer that is missing from this array.

 
# Example 1:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

# Example 2:
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

# Constraints:
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length


from typing import List
def findKthPositive(arr: List[int], k: int) -> int:
    arr = [0] + arr
    count = 0
    for i in range(1, len(arr)):
        tmp = arr[i] - arr[i - 1] - 1
        if count + tmp < k:
            count += tmp
        else:
            return arr[i - 1] + k - count

    return arr[-1] + k - count



assert(findKthPositive([2,3,4,7,11], 5) == 9)
assert(findKthPositive([2,3,4,7,11], 6) == 10)
assert(findKthPositive([1,2,3,4], 2) == 6)
assert(findKthPositive([3], 2) == 2)
assert(findKthPositive([1,13,18], 17) == 20)



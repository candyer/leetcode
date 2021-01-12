# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3600/


# Merge Sorted Array


# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively. 
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

 
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
 

# Constraints:
# 0 <= n, m <= 200
# 1 <= n + m <= 200
# nums1.length == m + n
# nums2.length == n
# -10^9 <= nums1[i], nums2[i] <= 10^9


from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    cur = len(nums1) - 1
    m -= 1
    n -= 1
    while cur >= 0:
        if m < 0:
            nums1[cur] = nums2[n]
            n -= 1
        elif n < 0:
            nums1[cur] = nums1[m]
            m -= 1
        else:
            if nums1[m] >= nums2[n]:
                nums1[cur] = nums1[m]
                m -= 1
            else:
                nums1[cur] = nums2[n]
                n -= 1
        cur -= 1


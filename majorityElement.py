# Leetcode 169 -- Majority Element 
# https://leetcode.com/problems/majority-element/#/description

# Given an array of size n, find the majority element. The majority element is the element that 
# appears more than n/2 times.

# You may assume that the array is non-empty and the majority element always exist in the array.

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []: return  None
    d = {}
    for num in nums:
        d[num] = d.get(num, 0)+1

    maxVal = max(d.values())
    for k,v in d.items():
        if v == maxVal:
            return k


assert majorityElement([2,4,2,6,2]) == 2
assert majorityElement([3,3,4,5,3]) == 3
assert majorityElement([1]) == 1

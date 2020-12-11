# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3562/、

# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3562/


# Remove Duplicates from Sorted Array II


# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
# Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

# Clarification:
# Confused why the returned value is an integer, but your answer is an array?
# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller.
# Internally you can think of this:
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
 

# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3]
# Explanation: Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the returned length.

# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3]
# Explanation: Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively. It doesn't matter what values are set beyond the returned length.
 

# Constraints:
# 0 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in ascending order.


from typing import List 
def removeDuplicates(nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
        return n
    count = 1
    for i in range(2, len(nums)):
        if nums[i] != nums[count] or nums[i] != nums[count - 1]:
            count += 1
            nums[count] = nums[i]
    return count + 1



from typing import List 
def removeDuplicates(nums: List[int]) -> int:
    i = 0
    for num in nums:
        if i < 2 or num != nums[i - 2]:
            nums[i] = num
            i += 1
    return i

assert(removeDuplicates([1,1,1,2,2,3,3,3,4,4,4,4]) == 8)
assert(removeDuplicates([1,1,1,2,2,3,3,3,4]) == 7)
assert(removeDuplicates([1,1,1,2,2,3]) == 5)
assert(removeDuplicates([0,0,1,1,1,1,2,3,3]) == 7)
assert(removeDuplicates([3,3,3,4,4,4]) == 4)
assert(removeDuplicates([3]) == 1)
assert(removeDuplicates([]) == 0)






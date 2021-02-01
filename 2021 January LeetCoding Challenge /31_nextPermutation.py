# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3623/

# Next Permutation


# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]

# Example 4:
# Input: nums = [1]
# Output: [1]

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100


from typing import List
def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    flag = True
    for i in range(n - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            flag = False
            j = i
            while j < n and nums[j] > nums[i - 1]:
                j += 1
            nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
            break

    k = 0 if flag else i
    for i in range((n - k) // 2):
        nums[k + i], nums[n - 1 - i] = nums[n - 1 - i], nums[k + i]


print(nextPermutation([1,2,3])) #[1,3,2])
print(nextPermutation([3,2,1])) #[1,2,3])
print(nextPermutation([1,1,5])) #[1,5,1])
print(nextPermutation([1])) #[1])
print(nextPermutation([4,7,6,5,3,1])) #[5,1,3,4,6,7])
print(nextPermutation([4,3,2,1])) #[1,2,3,4])

# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3528/


# Permutations II

# Given a collection of numbers, nums, that might contain duplicates, 
# return all possible unique permutations in any order.

# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
# Constraints:
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

from typing import List

def permuteUnique(nums: List[int]) -> List[List[int]]:
    res = []
    
    def dfs(nums, path):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
    nums.sort()
    dfs(nums, [])
    return res
    

assert(permuteUnique([1,1,2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]])
assert(permuteUnique([1,2,3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])









#https://leetcode.com/problems/permutations/#/description

# 46. Permutations

# Given an array nums of distinct integers, 
# return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]
 
# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) == 1: return [nums]  
    
    ans = []  
    for i in range(len(nums)):  
        for j in permute(nums[:i] + nums[i + 1:]):  
            ans.append([nums[i]] + j)  
    return ans  



from typing import List
def permute(nums: List[int]) -> List[List[int]]:
    def dfs(visited, path):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i, num in enumerate(nums):
            if not visited[i]:
                visited[i] = True
                path.append(num)
                dfs(visited, path)
                visited[i] = False
                path.pop()            
    res = []
    dfs([False] * len(nums), [])
    return res
     
assert(permute([1,2,3])==[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])


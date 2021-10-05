# https://leetcode.com/problems/subsets-ii/

# 90. Subsets II

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

############################################
############### Cascading ##################
############################################
def subsetsWithDup(nums):
    res = [[]]
    nums.sort()
    print(nums)
    for num in nums: 
        res += [ i + [num] for i in res if i + [num] not in res]
    return res


def subsetsWithDup(nums):
    res = {tuple()}
    nums.sort()
    for num in nums:
        res |= {subset + (num, ) for subset in res}
    return res

############################################
############### Backtracking ###############
############################################
def subsetsWithDup(nums):
    def backtrack(start, curr):
        res.append(curr)
        print(curr)
        for i in range(start, n):
            if i <= start or nums[i - 1] != nums[i]:
                backtrack(i + 1, curr + [nums[i]])
    res = []
    nums.sort()
    n = len(nums)
    backtrack(0, [])
    return res

############################################
### Lexicographic (Binary Sorted) Subsets ##
############################################
def subsetsWithDup(nums):
    n = len(nums)
    nums.sort()
    res = set()
    for mask in range(1 << n):
        subset = [nums[i] for i in range(n) if mask >> i & 1 ]
        res.add(tuple(subset))
    return res

print(subsetsWithDup([1,2,2]))
print(subsetsWithDup([0]))







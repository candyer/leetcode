#https://leetcode.com/problems/permutations/#/description
# 46. Permutations

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums)==1: return [nums]  
    
    ans=[]  
    for i in range(len(nums)):  
        for j in permute(nums[:i]+nums[i+1:]):  
            ans.append([nums[i]]+j)  
    return ans  

print permute([1,2,3]) #[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

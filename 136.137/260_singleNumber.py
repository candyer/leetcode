# leetcode 136 -- Single Number  Difficulty: Medium

# Given an array of integers, every element appears twice except for one. 
# Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    for key,val in d.items():
        if val == 1:
            return key

print singleNumber([1,1,2,2,3]) #3
print singleNumber([98,45,76,45,100,45,98]) #100
print singleNumber([]) #None


# leetcode 137 -- Single Number II  Difficulty: Medium

# Given an array of integers, every element appears three times except for one. 
# Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

def singleNumber2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []: return 0
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    for key,val in d.items():
        if val == 1:
            return key

print singleNumber2([4,3,6,5,3,4,6,6,3,4]) #5
print singleNumber2([])



# leetcode 260 -- Single Number III  Difficulty: Medium

# Given an array of numbers nums, in which exactly two elements appear only once 
# and all the other elements appear exactly twice. 
# Find the two elements that appear only once.
# For example:

# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. 
# Could you implement it using only constant space complexity?

def singleNumber3(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if nums == []: return [0,0]
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    res = []
    for key,val in d.items():
        if val == 1:
            res.append(key)
    return res

print singleNumber3([1,2,1,3,2,5]) #[3,5]
print singleNumber3([]) #[0,0]



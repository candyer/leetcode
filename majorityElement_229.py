# Leetcode 229 -- Majority Element II
# https://leetcode.com/problems/majority-element-ii/description/

# Given an integer array of size n, find all elements that appear more thann/3 times. 
# The algorithm should run in linear time and in O(1) space.

# Hint:
# How many majority elements could it possibly have?
# Do you have a better hint? Suggest it!

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # # #solution 1, linear time in O(n) space
    # d = {}
    # for num in nums:
    #     d[num] = d.get(num, 0)+1

    # n = len(nums)
    # res = []
    # for k,v in d.items():
    #     if v > n / 3:
    #         res.append(k)
    # return res

    #solution 2, linear time and O(1) space
    a = b = None
    c1 = c2 = 0
    for num in nums:
        if a == num:
            c1 += 1
        elif b == num:
            c2 += 1
        elif c1 == 0:
            a, c1 = num, 1
        elif c2 == 0:
            b, c2 = num, 1
        else:
            c1, c2 = c1 - 1, c2 - 1
        # print num, a,b, c1,c2
    size = len(nums)
    return [n for n in (a, b) if n is not None and nums.count(n) > size / 3]


print majorityElement([])
assert majorityElement([]) == []
assert majorityElement([1]) == [1]
assert majorityElement([1,1,2,2,3,3]) == []
print majorityElement([1,1,1,2,2,2,3])




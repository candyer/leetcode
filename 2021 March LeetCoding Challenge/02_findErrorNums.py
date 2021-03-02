# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658/

# Set Mismatch


# You have a set of integers s, which originally contains all the numbers from 1 to n. 
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
# which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]

# Example 2:
# Input: nums = [1,1]
# Output: [1,2]
 
# Constraints:
# 2 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^4

from typing import List
def findErrorNums(nums: List[int]) -> List[int]:
    '''
    Time Complexity: O(nlogn) (sort)
    Space Complexity: O(n)
    '''
    n = len(nums)
    nums.sort()
    dup = miss = 1
    for i in range(1, n):
        diff = nums[i] - nums[i - 1]
        if diff == 0:
            dup = nums[i]
        elif diff > 1:
            miss = nums[i] - 1
    if nums[-1] < n:
        miss = n
    return [dup, miss]


from typing import List
def findErrorNums(nums: List[int]) -> List[int]:
    '''
    Time Complexity: O(n) (sum)
    Space Complexity: O(1)
    '''
    n = len(nums)
    espected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    set_sum = sum(set(nums))
    dup = actual_sum - set_sum
    miss = espected_sum - set_sum
    return [dup, miss]  


assert(findErrorNums([1,2,2,4]) == [2,3])
assert(findErrorNums([1,1]) == [1,2])
assert(findErrorNums([5,3,1,4,4]) == [4,2])
assert(findErrorNums([2,2]) == [2,1])
assert(findErrorNums([1,5,3,2,2,7,6,4,8,9]) == [2,10])





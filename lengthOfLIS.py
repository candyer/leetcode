# leetcode 300 -- Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/description/

# Given an unsorted array of integers, find the length of longest increasing subsequence.
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. 
# Note that there may be more than one LIS combination, 
# it is only necessary for you to return the length.

# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?



def lengthOfLIS(nums):
    """
    type nums: List[int],rtype: int
    there may be more than one LIS combination, it's only necessary to return the len
    e.g. [10, 9, 2, 5, 3, 7, 101, 18] --> [2, 3, 7, 101] --> 4
    complexity should be O(n^2) or O(nlogn) 
    """
    #solution 1  Brute force
    # if nums == []:
    #     return 0
    # size = len(nums)
    # res = [1] * size
    # for i in range(size): 
    #     for j in range(i):
    #         if nums[i] > nums[j]:
    #             res[i] = max(res[i],res[j]+1)
    # return max(res)


    #solution 2  Dynamic Programming
    n = len(nums)
    dp = []
    for x in range(n):
        low, high = 0, len(dp) - 1
        while low <= high:
            mid = (low + high) / 2
            if dp[mid] >= nums[x]:
                high = mid - 1
            else:
                low = mid + 1

        if low >= len(dp):
            dp.append(nums[x])

        else:
            dp[low] = nums[x]
    # print dp
    return len(dp)

print lengthOfLIS([2,5,1])
# print lengthOfLIS([3,4,-1,5,8,2,3,12,7,9,10]) 
# assert lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
# assert lengthOfLIS([4,5,3,7,101,2]) == 4
# assert lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]) == 6
# assert lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]) == 6
# assert lengthOfLIS([50,51,55,35,38,42]) == 3
# assert lengthOfLIS([4,5,3,7,101,2]) == 4



# import unittest

# class MyTest(unittest.TestCase):     
#     def test_longesr(self):
#         self.assertEqual(lengthOfLIS([]), 0)
#         self.assertEqual(lengthOfLIS([4]), 1)
#         self.assertEqual(lengthOfLIS([10, 9, 5, 3, 7, 101, 18]), 3)
#         self.assertEqual(lengthOfLIS([4, 5, 3, 7, 101, 2]), 4)
#         self.assertEqual(lengthOfLIS([5,4,3,2,1]), 1)
#         self.assertEqual(lengthOfLIS([18, 55, 66, 2, 3, 54]), 3)
#         self.assertEqual(lengthOfLIS([20, 30, 40, 3, 5, 29]), 3)
#         self.assertEqual(lengthOfLIS([50, 51, 55, 35, 38, 42]), 3)
#         self.assertEqual(lengthOfLIS([1, 7, 3, 2]), 2)
#         self.assertEqual(lengthOfLIS([1, 1, 5, 4, 3, 2]), 2)
#         self.assertEqual(lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]), 6)

# if __name__ == '__main__':
#     unittest.main()


# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.003s

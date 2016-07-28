# https://leetcode.com/problems/two-sum/

#Given an array of integers, find two numbers such that they add up to a specific target number.
#The function twoSum should return indices of the two numbers such that they add up to the target, 
#where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#You may assume that each input would have exactly one solution.
#e.g.
#Input: numbers={2, 7, 11, 15}, target=9
#Output: index1=1, index2=2

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    val_index = {}
    for i in xrange(len(nums)): 
        if target-nums[i] in val_index:
            return [val_index[target-nums[i]]+1, i+1]
        val_index[nums[i]] = i

import unittest

class MyTest(unittest.TestCase):  
    def setUp(self):
        self.nums1 = [2,3,5,4,1,7]
        self.nums2 = [7,8,3,1,2,9,5,10,4]
        self.nums3 = [1,2,7,11,15]
        self.nums4 = [0,4,3,0]
        self.nums5 = [4,0,3,7,0]
        self.nums6 = [-3,4,3,90]
        self.nums7 = [2,1,9,4,4,56,90,3]
        self.nums8 = [3,5,6,5,4,0]
        self.nums9 = [3,5,8,3,4,0]

    def test_twosum1(self):
        self.assertEqual(twoSum(self.nums1, 6),[1,4])
        self.assertEqual(twoSum(self.nums2, 6),[4,7]) 
        self.assertEqual(twoSum(self.nums3, 9),[2,3])

    def test_twosum2(self):
        self.assertEqual(twoSum(self.nums4, 0),[1,4])
        self.assertEqual(twoSum(self.nums5, 0),[2,5])
        self.assertEqual(twoSum(self.nums6, 0),[1,3])

    def test_twosum3(self):
        self.assertEqual(twoSum(self.nums7, 8),[4,5]) 
        self.assertEqual(twoSum(self.nums8, 10),[2,4]) 
        self.assertEqual(twoSum(self.nums9, 6),[1,4])

if __name__ == '__main__':
    unittest.main()

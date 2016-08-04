# https://leetcode.com/problems/3sum/

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
# Note: The solution set must not contain duplicate triplets.

class Solution(object):
    def make_counter(self,nums):
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        return d
    
    def threeSum(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []
        counter = self.make_counter(nums)
        res = []
        choices = sorted(counter.keys())
    
        for i, num_a in enumerate(choices):
            if num_a > 0: break
            counter[num_a] = counter[num_a] - 1
            for j in xrange(i, len(choices)):            
                num_b = choices[j]
                if counter[num_b] == 0: continue
    
                total = -(num_a + num_b)
                if total < 0: break
                counter[num_b] = counter[num_b] - 1
    
                if total >= num_b and counter.get(total, 0) > 0:
                    res.append([num_a, num_b, total])
                counter[num_b] = counter[num_b] + 1
            counter[num_a] = counter[num_a] + 1
    
        return res

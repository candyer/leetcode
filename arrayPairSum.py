# https://leetcode.com/contest/leetcode-weekly-contest-29/problems/array-partition-i/

def arrayPairSum(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	nums.sort()
	res = 0
	for i in range(0, len(nums), 2):
		res += nums[i]
	return res

print arrayPairSum([1,4,2,3])

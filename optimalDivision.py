# https://leetcode.com/contest/leetcode-weekly-contest-28/problems/optimal-division/

def optimalDivision(nums):
	"""
	:type nums: List[int]
	:rtype: str
	"""
	n = len(nums)
	s = map(str, nums)
	res = [s[0]]
	if n > 2:
		res.append('/(')
		for char, slash in zip(s[1:], ['/'] * (n - 1)):
			res.append(char)
			res.append(slash)
		res[-1] = ')'
	elif n > 1:
		res.append('/')
		res.append(s[-1])
	return ''.join(res)



print optimalDivision([1000,100,10,2]) #1000/(100/10/2)
print optimalDivision([1,10,100,1000,2]) #1/(10/100/1000/2)
print optimalDivision([1000]) #1000
print optimalDivision([1000,2]) #1000/2

# https://leetcode.com/problems/assign-cookies/description/

# 455. Assign Cookies

# Assume you are an awesome parent and want to give your children some cookies. 
# But, you should give each child at most one cookie. Each child i has a greed factor gi, 
# which is the minimum size of a cookie that the child will be content with; and each 
# cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, 
# and the child i will be content. Your goal is to maximize the number of your content 
# children and output the maximum number.

# Note:
# You may assume the greed factor is always positive. 
# You cannot assign more than one cookie to one child.

# Example 1:   Input: [1,2,3], [1,1]   Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
# And even though you have 2 cookies, since their size is both 1, you could only make the child 
# whose greed factor is 1 content.
# You need to output 1.

# Example 2:   Input: [1,2], [1,2,3]   Output: 2
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
# You have 3 cookies and their sizes are big enough to gratify all of the children, 
# You need to output 2.


def findContentChildren1(g, s):
	"""
	:type g: List[int] children's greed factor
	:type s: List[int] cookie size
	:rtype: int
	"""
	g = sorted(g, reverse=True)
	s = sorted(s, reverse=True)
	res = i = j = tmp = 0
	m, n = len(g), len(s)
	while i < m:
		j = tmp
		while j < n:
			if g[i] > s[j]:
				break
			else:
				res += 1
				tmp = j + 1
				break
		i += 1
	return res

def findContentChildren2(g, s):
	"""
	:type g: List[int] children's greed factor
	:type s: List[int] cookie size
	:rtype: int
	"""
	g = sorted(g, reverse=True)
	s = sorted(s, reverse=True)
	res = i = j = 0
	m, n = len(g), len(s)
	while i < m and j < n:
		if g[i] > s[j]:
			i += 1
		else:
			res += 1
			i += 1
			j += 1
	return res


assert findContentChildren2([1,2,3,7,8,100, 100000],[1,5, 99999, 7878]) == 4
assert findContentChildren2([10, 8, 6, 4, 2], [100, 7, 3, 3, 1]) == 3
assert findContentChildren2([1,2,3], [1,1]) == 1
assert findContentChildren2([1,2,3,6], [5, 2]) == 2
assert findContentChildren2([2,3], [1,2,4]) == 2


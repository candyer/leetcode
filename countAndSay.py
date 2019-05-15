# https://leetcode.com/problems/count-and-say/description/


# 38. Count and Say

# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 <= n <= 30, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

# Example 1:
# Input: 1
# Output: "1"

# Example 2:
# Input: 4
# Output: "1211"

# def f(num):
# 	array = list(num) + ['*']
# 	n = len(array)
# 	res = []
# 	count = 1
# 	for i in range(n - 1):
# 		if array[i] == array[i + 1] :
# 			count += 1
# 		else:
# 			res.append(str(count))
# 			res.append(array[i])
# 			count = 1
# 	return ''.join(res)


# def solve():
# 	res = ['1', '11', '21', '1211', '111221']
# 	for i in range(6, 31):
# 		res.append(f(res[i - 2]))
# 	return res

# def countAndSay(n):
# 	"""
# 	:type n: int
# 	:rtype: str
# 	"""
# 	return solve()[n - 1]


def countAndSay(n):
	"""
	:type n: int
	:rtype: str
	"""
	res = '1'
	for i in range(n - 1):
		cur = res[0]
		count = 1
		tmp = []
		for i in range(1, len(res)):
			if res[i] == cur:
				count += 1
				continue
			tmp.append(str(count))
			tmp.append(cur)
			cur = res[i]
			count = 1
		tmp.append(str(count))
		tmp.append(cur)
		res = ''.join(tmp)
	return res

assert countAndSay(5) == '111221'
assert countAndSay(7) == '13112221'
assert countAndSay(10) == '13211311123113112211'




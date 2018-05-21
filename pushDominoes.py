# https://leetcode.com/problems/push-dominoes/description/

# 838. Push Dominoes

# There are N dominoes in a line, and we place each domino vertically upright.
# In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left.
# Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the 
# balance of the forces.
# For the purposes of this question, we will consider that a falling domino expends no additional 
# force to a falling or already fallen domino.
# Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to 
# the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th 
# domino has not been pushed.
# Return a string representing the final state. 

# Example 1:
# Input: ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."

# Example 2:
# Input: "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.

# Note:
# 0 <= N <= 10^5
# String dominoes contains only 'L', 'R' and '.'

############################
##### first solution #######
############################
def pushDominoes(dominoes):
	"""
	:type dominoes: str
	:rtype: str
	"""
	n = len(dominoes)
	dominoes = ['L'] + list(dominoes) + ['R']
	array = dominoes[:]
	i = 0
	while i < n + 1:
		if dominoes[i] == 'R' and dominoes[i + 1] == '.':
			array[i] = "R"
			j = i + 1
			while dominoes[j] == '.':
				j += 1
				if dominoes[j] == 'L':
					count = j - i -  1
					mid = (j + i + 1) / 2
					array[i + 1: mid] = ['R'] * (count / 2 )
					if count % 2:
						array[mid + 1: j] = ['L'] * (count / 2 )
					else:
						array[mid: j] = ['L'] * (count / 2 )
						
				elif dominoes[j] == 'R':
					for k in range(i + 1, j + 1):
						array[k] = 'R'
			i = j - 1
		elif dominoes[i] == 'L' and dominoes[i + 1] == '.':
			array[i] = "L"
			j = i + 1
			while dominoes[j] == '.':
				j += 1
				if dominoes[j] == 'L':
					for k in range(i + 1, j + 1):
						array[k] = 'L'
			i = j - 1
		i += 1
	return ''.join(array[1:-1])



#####################################
## elegent solution from editorial ##
#####################################

def pushDominoes(dominoes):
	symbols = [(-1, 'L')] + [(i, x) for i, x in enumerate(dominoes) if x != '.'] + [(len(dominoes), 'R')]

	res = list(dominoes)
	for (i, x), (j, y) in zip(symbols, symbols[1:]):
		if x == y: # RR / LL
			for k in xrange(i + 1, j):
				res[k] = x
		elif x > y: #RL
			for k in xrange(i + 1, j):
				res[k] = '.LR'[cmp(k - i, j - k)]
	return "".join(res)

# The method cmp() returns the sign of the difference of two numbers : -1 if x < y, 0 if x == y, or 1 if x > y.
assert cmp(1, 2) == -1
assert cmp(1, 1) == 0
assert cmp(1, 0) == 1




assert pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL.."
assert pushDominoes(".L.R...LR.L..") == "LL.RR.LLR.L.."
assert pushDominoes(".R...RL...LR.L..") == ".RRRRRLLLLLR.L.."
assert pushDominoes(".R.L...LR.L..") == ".R.LLLLLR.L.."
assert pushDominoes("..L.RRLL.R") == "LLL.RRLL.R"
assert pushDominoes(".L.R...LR.L..") == "LL.RR.LLR.L.."
assert pushDominoes("RR.L") == "RR.L"
assert pushDominoes("R.L") == "R.L"
assert pushDominoes("") == ""
assert pushDominoes("LLL") == "LLL"
assert pushDominoes("RR") == "RR"
assert pushDominoes("LRR..RR..R") == "LRRRRRRRRR"
assert pushDominoes("..LL..RR.") == "LLLL..RRR"

# import random
# array = []
# for i in range(10):
# 	array.append(random.choice(['L', 'R', '.']))
# print ''.join(array)
# print pushDominoes(array)

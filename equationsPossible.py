# https://leetcode.com/problems/satisfiability-of-equality-equations/description/


# 990. Satisfiability of Equality Equations


# Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 
# and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) 
# that represent one-letter variable names.

# Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.


# Example 1:
# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to 
# assign the variables to satisfy both equations.

# Example 2:
# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

# Example 3:
# Input: ["a==b","b==c","a==c"]
# Output: true

# Example 4:
# Input: ["a==b","b!=c","c==a"]
# Output: false

# Example 5:
# Input: ["c==c","b==d","x!=z"]
# Output: true
 

# Note:
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] and equations[i][3] are lowercase letters
# equations[i][1] is either '=' or '!'
# equations[i][2] is '='



from collections import defaultdict
def equationsPossible(equations):
	"""
	:type equations: List[str]
	:rtype: bool
	"""
	equal = defaultdict(set)
	notequal = []

	for equation in equations:
		first, second = equation[0], equation[3]
		sign = equation[1:3]
		
		if sign == '==': 
			if first != second:
				equal[first].add(second)
				equal[second].add(first)
				for aa in equal[first]:
					if not second in equal[aa] and aa != second:
						equal[aa].add(second)
						if not 11 in equal[second]:
							equal[second].add(aa)	
				for bb in equal[second]:
					if not first in equal[bb] and bb != first:
						equal[bb].add(first)
						if not bb in equal[first]:
							equal[first].add(bb)				
		else:
			notequal.append(equation)
		
	for equation in notequal:
		first, second = equation[0], equation[3]
		if first in equal and second in equal[first]:
			return False
		elif second in equal and first in equal[second]:
			return False
		elif first == second:
			return False
	return True


assert equationsPossible(["e!=c","b!=b","b!=a","e==d"]) == False
assert equationsPossible(["a==b","b!=a"]) == False
assert equationsPossible(["b==a","a==b"]) == True
assert equationsPossible(["a==b","b==c","a==c"]) == True
assert equationsPossible(["a==b","b!=c","c==a"]) == False
assert equationsPossible(["c==c","b==d","x!=z"]) == True
assert equationsPossible(["c==c","b==d","x!=z", 'c==b', 'x==c', 'c!=d']) == False
assert equationsPossible(["a==b","b!=d","b==c", "a!=x"]) == True
assert equationsPossible(["a==b","b!=d","b!=b"]) == False






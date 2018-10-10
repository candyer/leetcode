# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/


# 744. Find Smallest Letter Greater Than Target

# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, 
# find the smallest element in the list that is larger than the given target.

# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

# Examples:
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"

# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"

# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"

# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"

# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"

# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
# Note:
# letters has a length in range [2, 10000].
# letters consists of lowercase letters, and contains at least 2 unique letters.
# target is a lowercase letter.



#################
####solution 1###
#################
def nextGreatestLetter(letters, target):
	"""
	:type letters: List[str]
	:type target: str
	:rtype: str
	"""
	res = letters[0]
	for letter in letters:
		if letter > target:
			res = letter
			break
	return res



#################
####solution 2###
#################
def nextGreatestLetter(letters, target):
	"""
	:type letters: List[str]
	:type target: str
	:rtype: str
	"""
	n = len(letters)
	low, high = 0, n
	while low < high:
		mid = (low + high) / 2
		if letters[mid] <= target:
			low = mid + 1
		else:
			high = mid
	return letters[low % n]


assert nextGreatestLetter(["c", "f", "j"], "a") == "c"
assert nextGreatestLetter(["c", "f", "j"], "c") == "f"
assert nextGreatestLetter(["c", "f", "j"], "d") == "f"
assert nextGreatestLetter(["c", "f", "j"], "g") == "j"
assert nextGreatestLetter(["c", "f", "j"], "j") == "c"
assert nextGreatestLetter(["c", "f", "j"], "k") == "c"







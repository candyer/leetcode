# https://leetcode.com/problems/maximum-number-of-balloons/description/

# 1189. Maximum Number of Balloons


# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 
# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0
 
# Constraints:
# 1 <= text.length <= 10^4
# text consists of lower case English letters only.

from collections import defaultdict
def maxNumberOfBalloons(text):
	"""
	:type text: str
	:rtype: int
	"""
	d = {'a': 1, 'b': 1, 'l': 2, 'o': 2, 'n': 1}
	count = defaultdict(int)
	for c in text:
		if c in 'ablon':
			count[c] += 1
	res = float('inf')
	for k, v in d.items():
		res = min(res, count[k] / v)
	return res


assert maxNumberOfBalloons("nlaebolko") == 1
assert maxNumberOfBalloons("loonbalxballpoon") == 2
assert maxNumberOfBalloons("leetcode") == 0
assert maxNumberOfBalloons("lloo") == 0

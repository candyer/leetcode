# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3699/

# Determine if String Halves Are Alike


# You are given a string s of even length. Split this string into two halves of equal lengths, 
# and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 
# 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

 
# Example 1:
# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

# Example 2:
# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.

# Example 3:
# Input: s = "MerryChristmas"
# Output: false

# Example 4:
# Input: s = "AbCdEfGh"
# Output: true
 

# Constraints:
# 2 <= s.length <= 1000
# s.length is even.
# s consists of uppercase and lowercase letters.

from collections import Counter
def halvesAreAlike(s: str) -> bool:
	mid = len(s) // 2
	s = s.lower()
	left_dict, right_dict = Counter(s[:mid]), Counter(s[mid:])
	l = r = 0
	for c in 'aeiou':
		l += left_dict[c]
		r += right_dict[c]
	return l == r

from collections import Counter
def halvesAreAlike(s: str) -> bool:
	mid, s, vowels = len(s) // 2, s.lower(), set(["a","e","i","o","u"])
	left, right = s[:mid], s[mid:]
	countl = countr = 0
	for i in range(mid):
		if left[i] in vowels:
			countl += 1
		if right[i] in vowels:
			countr += 1
	return countl == countr


assert(halvesAreAlike("book") == True)
assert(halvesAreAlike("textbook") == False)
assert(halvesAreAlike("MerryChristmas") == False)
assert(halvesAreAlike("AbCdEfGh") == True)






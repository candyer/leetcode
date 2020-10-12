# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3492/


# Buddy Strings

# Given two strings A and B of lowercase letters, return true if you can swap two letters in A 
# so the result is equal to B, otherwise, return false.
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and 
# swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


# Example 1:
# Input: A = "ab", B = "ba"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.

# Example 2:
# Input: A = "ab", B = "ab"
# Output: false
# Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.

# Example 3:
# Input: A = "aa", B = "aa"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.

# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true

# Example 5:
# Input: A = "", B = "aa"
# Output: false
 
# Constraints:
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist of lowercase letters.




# from collections import Counter
# def buddyStrings(A: str, B: str) -> bool:
# 	n1, n2 = len(A), len(B)
# 	if n1 != n2:
# 		return False
# 	d1, d2 = Counter(A), Counter(B)
# 	if d1 != d2:
# 		return False
# 	count = 0
# 	for a, b in zip(A, B):
# 		if a != b:
# 			count += 1
# 	if count == 0 and len(set(A)) < n1 or count == 2:
# 		return True
# 	return False




def buddyStrings(A: str, B: str) -> bool:
	n1, n2 = len(A), len(B)
	if n1 != n2 or set(A) != set(B): 
		return False       
	if A == B:
		return n1 - len(set(A)) >= 1
	else:     
		indices = []
		count = 0
		for i in range(n1):
			if A[i] != B[i]:
				count += 1
				indices.append(i)       
			if count > 2:
				return False     
		return A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]



assert(buddyStrings("ab", "ba") == True)
assert(buddyStrings("ab", "ab") == False)
assert(buddyStrings("aa", "aa") == True)
assert(buddyStrings("aaaaaaabc", "aaaaaaacb") == True)
assert(buddyStrings("", "aa") == False)
assert(buddyStrings("abcaa", "abcbb") == False)





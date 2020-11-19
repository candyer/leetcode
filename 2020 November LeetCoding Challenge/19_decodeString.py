# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3536/

# Decode String

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
# is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for 
# those repeat numbers, k. For example, there won't be input like 3a or 2[4].


# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
 

# Constraints:
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

# isalnum():returns True if all characters in the string are alphanumeric(alphabets / numbers). Returns False otherwise.
# isalpha():returns True if all characters in the string are alphabets. Returns False otherwise.
# isdigit():returns True if all characters in a string are digits. Returns False otherwise.



def decodeString(s: str) -> str:
	stack = []
	for c in s:
		if c == ']':
			tmp = []
			count = 0
			while stack:
				cc = stack.pop()
				if cc.isalpha():
					tmp.append(cc)
				else:
					break
			i = 1
			while stack:    
				if stack[-1].isdigit(): 
					cc = stack.pop()
					if cc.isdigit():
						count += int(cc) * i
						i *= 10
				else:
					break
			stack.append(count * ''.join(tmp[::-1]))
		else:
			stack.append(c)
	return ''.join(stack)




def decodeString(s: str) -> str:
	stack = []
	num = string = ''
	for c in s:
		if c == '[':
			stack.append(string)
			stack.append(int(num))
			num = string = ''
		elif c == ']':
			count = stack.pop()
			prev_str = stack.pop()
			string = prev_str + string * count
		elif c.isdigit():
			num += c
		else:
			string += c

	return string


	

assert(decodeString("3[a2[bc4[z]]]") == 'abczzzzbczzzzabczzzzbczzzzabczzzzbczzzz')
assert(decodeString("3[a]2[bc]") == "aaabcbc")
assert(decodeString("3[a2[c]]") == "accaccacc")
assert(decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
assert(decodeString("abc3[cd]xyz") == "abccdcdcdxyz")
assert(decodeString("3[a12[c]]")=="accccccccccccaccccccccccccacccccccccccc")
assert(decodeString("a") == 'a')








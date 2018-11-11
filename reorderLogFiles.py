# https://leetcode.com/problems/reorder-log-files/description/


# 937. Reorder Log Files


# You have an array of logs.  Each log is a space delimited string of words.

# For each log, the first word in each log is an alphanumeric identifier.  Then, either:

# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, 
# with the identifier used in case of ties.  The digit-logs should be put in their original order.

# Return the final order of the logs.

 

# Example 1:
# Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 

# Note:
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the identifier.


def reorderLogFiles(logs):
	"""
	:type logs: List[str]
	:rtype: List[str]
	"""
	letter_logs, digit_logs = [], []
	for i, log in enumerate(logs):
		if log[-1].isdigit():
			digit_logs.append(log)
		else:
			letter_logs.append(log)
	letter_logs.sort(key = lambda x: x.split()[1:])
	return letter_logs + digit_logs



print reorderLogFiles([]) == []
print reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]) == ['g1 act car', 'a8 act zoo', 'ab1 off key dog', 'a1 9 2 3 1', 'zo4 4 7']
print reorderLogFiles(["qi ir oo i", "cp vnzw i", "0 fkbikbts", "4 j trouka", "gn j q al", "5r w wgqc", "m8 x haje", "fg 28694 6", "i gf mwdoa", "ao 0850716"])
# ['0 fkbikbts', 'i gf mwdoa', 'qi ir oo i', 'gn j q al', '4 j trouka', 'cp vnzw i', '5r w wgqc', 'm8 x haje', 'fg 28694 6', 'ao 0850716']








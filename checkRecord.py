# https://leetcode.com/contest/leetcode-weekly-contest-28/problems/student-attendance-record-i/

def checkRecord(s):
	"""
	:type s: str
	:rtype: bool
	"""
	return s.count('A') <= 1 and s.count('LLL') == 0

print checkRecord("LLAA") # False
print checkRecord("PPPLLPAA") # False
print checkRecord("PPALLP") # True
print checkRecord("PPALLL") # False

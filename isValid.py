class Solution(object):
    def isValid(self,s):
        """
        :type s: str
        :rtype: bool
        """
        symbles = {"(": ")","{" :"}", "[":"]"}
        stack = []
        for c in s:
            if c in symbles:
                stack.append(c)
            else:
                if not stack or symbles[stack.pop()] != c:
                    return False
        return not stack

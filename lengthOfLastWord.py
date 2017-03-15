   # https://leetcode.com/problems/length-of-last-word/#/description
    
  def lengthOfLastWord(s):
      """
      :type s: str
      :rtype: int
      """
      listOfStrings = s.split()
      if listOfStrings == []: return 0
      return len(listOfStrings[-1])

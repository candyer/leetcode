# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3706/

# Flatten Nested List Iterator


# You are given a nested list of integers nestedList. Each element is either an integer or 
# a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
# Implement the NestedIterator class:
# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list 
# nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and 
# false otherwise.
 

# Example 1:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, 
# the order of elements returned by next should be: [1,1,2,1,1].

# Example 2:
# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, 
# the order of elements returned by next should be: [1,4,6].
 

# Constraints:
# 1 <= nestedList.length <= 500
# The values of the integers in the nested list is in the range [-10^6, 10^6].



# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

from collections import deque
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nums = deque()
        self.flatten(nestedList)
        self.n = len(self.nums)

    def flatten(self, arr):
        for elem in arr:
            if elem.isInteger():
                self.nums.append(elem.getInteger())
            else:
                self.flatten(elem.getList())
        
    
    def next(self) -> int:
        self.n -= 1
        return self.nums.popleft()
        
    
    def hasNext(self) -> bool:
        return self.n > 0
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())









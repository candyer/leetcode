# https://leetcode.com/problems/min-stack/description/

# 155. Min Stack

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack(object):

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.array = []
		self.count = 0
		

	def push(self, x):
		"""
		:type x: int
		:rtype: None
		"""
		mini = self.getMin()
		if mini == None or mini > x:
			mini = x
		self.array.append((x, mini))
		self.count += 1
		

	def pop(self):
		"""
		:rtype: None
		"""
		self.array.pop()
		self.count -= 1
		
		
	def top(self):
		"""
		:rtype: int
		"""
		if self.count == 0:
			return None
		return self.array[-1][0]
		

	def getMin(self):
		"""
		:rtype: int
		"""
		if not self.array:
			return None
		return self.array[-1][1]
		


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

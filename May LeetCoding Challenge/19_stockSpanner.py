# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3334/


# Online Stock Span

# Write a class StockSpanner which collects daily price quotes for some stock, 
# and returns the span of that stock's price for the current day.

# The span of the stock's price today is defined as the maximum number of consecutive days 
# (starting from today and going backwards) for which the price of the stock was less than 
# or equal to today's price.

# For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], 
# then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

 

# Example 1:

# Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
# Output: [null,1,1,1,2,1,4,6]
# Explanation: 
# First, S = StockSpanner() is initialized.  Then:
# S.next(100) is called and returns 1,
# S.next(80) is called and returns 1,
# S.next(60) is called and returns 1,
# S.next(70) is called and returns 2,
# S.next(60) is called and returns 1,
# S.next(75) is called and returns 4,
# S.next(85) is called and returns 6.

# Note that (for example) S.next(75) returned 4, because the last 4 prices
# (including today's price of 75) were less than or equal to today's price.
 

# Note:

# Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
# There will be at most 10000 calls to StockSpanner.next per test case.
# There will be at most 150000 calls to StockSpanner.next across all test cases.
# The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.

class StockSpanner(object):
	def __init__(self):
		self.stack = []

	def next(self, price):
		count = 1
		while self.stack and self.stack[-1][0] <= price:
			count += self.stack.pop()[1]
		self.stack.append((price, count))
		return count

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next([100])
assert(param_1 == 1)
param_2 = obj.next([80])
assert(param_2 == 1)
param_3 = obj.next([60])
assert(param_3 == 1)
param_4 = obj.next([70])
assert(param_4 == 2)
param_5 = obj.next([60])
assert(param_5 == 1)
param_6 = obj.next([75])
assert(param_6 == 4)
param_7 = obj.next([85])
assert(param_7 == 6)







# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3464/


# Best Time to Buy and Sell Stock

# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one 
# share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# Example 2:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


# from typing import List
# def maxProfit(prices: List[int]) -> int:
# 	n = len(prices)
# 	if n <= 1:
# 		return 0
# 	mins = []
# 	mini = float('inf')
# 	for price in prices:
# 		if price < mini:
# 			mini = price
# 		mins.append(mini)

# 	price, mini = max(zip(prices, mins), key=lambda x: x[0] - x[1])
# 	return price - mini


from typing import List
def maxProfit(prices: List[int]) -> int:
	n = len(prices)
	if n <= 1:
		return 0
	max_profit = 0
	buy_price = prices[0]
	for i in range(1, n):
		if prices[i] < buy_price:
			buy_price = prices[i]
		else:
			max_profit = max(prices[i] - buy_price, max_profit)
	return max_profit

assert(maxProfit([7,1,5,3,6,4]) == 5)
assert(maxProfit([7,6,4,3,1]) == 0)
assert(maxProfit([1]) == 0)
assert(maxProfit([]) == 0)

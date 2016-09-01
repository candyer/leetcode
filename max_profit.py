
# leetcode 122 -- Best Time to Buy and Sell Stock II

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. 
# You may complete as many transactions as you like 
# (ie, buy one and sell one share of the stock multiple times). 
# However, you may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    ## solution one, O(n)
    if len(prices) <2: return 0

    new_list = []
    start = 0
    for i in range(len(prices)-1):
        if prices[i] > prices[i+1]:
            sublist = prices[start:i+1]
            start = i+1
            new_list.append(sublist) 

    if start != len(prices) -1:
        new_list.append(prices[start:])

    max_profit = 0
    for sublist in new_list:
        max_profit+= sublist[-1] - sublist[0]
    return max_profit


    ## solution two, O(n)
    if len(prices) <2: return 0

    new_list = []
    start = 0
    prices += [-1]
    for i in range(len(prices)-1):
        if prices[i] > prices[i+1]:
            sublist = prices[start:i+1]
            start = i+1
            new_list.append(sublist) 

    max_profit = 0
    for sublist in new_list:
        max_profit+= sublist[-1] - sublist[0]
    return max_profit


    ## solution three, O(n)
    return sum([x - y for x, y in zip(prices[1:], prices) if x > y])


print maxProfit([]) #0
print maxProfit([1]) #0
print maxProfit([1,2]) #1
print maxProfit([2,1]) #0
print maxProfit([2,3,3,9,9,1,9,5,9]) #19
print maxProfit([2,3,6,1,7,9,8,10]) #14
print maxProfit([2,3,6,1,7,9,8,10,7,9,3,6,7,9,2,8]) #28
print maxProfit([2,4,1]) #2
print maxProfit([9,4,7]) #3
print maxProfit([2,3,1,9,5,9]) #13
print maxProfit([1,2,4,7]) #6
import random
a = [random.randrange(400000) for _ in range(1000000)]
print maxProfit(a)

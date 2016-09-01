# Leetcode 123 -- Best Time to Buy and Sell Stock III

# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note:
# You may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).

def maxProfit(prices):
    ##solution one    Brute force  O(n^4)
    best = 0
    n = len(prices)
    for i in range(n):
        for j in range(i, n):
            profit1 = max(0, prices[j] - prices[i])
            for k in range(j, n):
                for l in range(k, n):
                    profit2 = max(0, prices[l] - prices[k])
                    total = profit1 + profit2
                    best = max(best, total)
    return best



    ##solution two  
    if len(prices)==0: return 0
    n = len(prices)

    before,after =[0]*n,[0]*n

    profit1 = prices[0]
    for i in range(1,n):
        profit1 = min(profit1, prices[i])
        before[i] = max((prices[i] - profit1), before[i-1])

    profit2 = prices[-1]
    for j in range(n-2,-1,-1):
        profit2 = max(profit2, prices[j])
        after[j] = max(after[j+1], profit2-prices[j])

    res = 0
    for k in range(len(before)):
        if res < before[k] + after[k]:
            res = before[k] + after[k]
    return res


print maxProfit([1,100]) #99
print maxProfit([]) #0
print maxProfit([2,3,6,1,7,9,8,10,7,9,3,6,7,9,2,8]) #15
print maxProfit([2,3,6,2,7,1,7,9,8,10]) #14
print maxProfit([2,3,6,2,7,10,1,11]) #18
print maxProfit([2,3,1,9,5,9]) #12
print maxProfit([1,2,4,7]) #6
print maxProfit([2,3,6,1,7,9,8,10,9,15,7,9,3,6,7,9,2,8]) #20
print maxProfit([1,4,3,6]) #6
print maxProfit([3,8,6,9]) #8
print maxProfit([750,804,899,845,957,462,609,876,276,918,812,535,782,873,39,426,421,480,663,120]) #1266
print maxProfit([639,153,426,456,209,529,556,388,312,845,989,32,561,93,755,118,19,818,107,534]) #1635
print maxProfit([1,6,4,7,5,8]) #9
print maxProfit([8,1,6,0,1,4,0,8,1,1,6,2,2,8,0,0,9,6,3,6]) #17
import random
a = [random.randrange(10000) for _ in range(200000)]
print maxProfit(a)

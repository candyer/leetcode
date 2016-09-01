# leetcode 121 -- Best Time to Buy and Sell Stock

# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    
    ## Solution one, O(n**2)

    profit = max_profit = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > 0:
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
    return max_profit
    


   ## Solution two, O(n)
   
    if len(prices) < 2: return 0
        
    mins = []
    small = smallest = prices[0]
    for i in range(len(prices)):
        small = min(small, prices[i])
        if smallest > small:
            smallest = small
        mins.append(smallest)

    profit = max_profit = 0
    for j in range(len(prices)):
        if prices[j] - mins[j] > 0:
            profit = prices[j] - mins[j]
            if profit > max_profit:
                max_profit = profit
    return max_profit



   ## Solution three, O(n)

    if len(prices) < 2: return 0
    
    maxes = []
    big = bigest = 0
    for i in range(len(prices)-1, -1, -1):
        big = max(big, prices[i])
        if bigest < big:
            bigest = big
        maxes.append(bigest)
    maxes.reverse() 

    profit = maxprofit = 0
    for j in range(len(prices)):
        if maxes[j] - prices[j] > 0:
            profit = maxes[j] - prices[j]
            if profit > maxprofit:
                maxprofit = profit
    return maxprofit



   ## Solution four, O(n)  
    if len(prices) < 2: return 0

    maxes = [None] * len(prices)
    big = float("-inf")
    for i in range(len(prices) -1, -1, -1):
        big = max(big, prices[i])
        maxes[i] = big

    profit = maxprofit = 0
    for j in range(len(prices)):
        if maxes[j] - prices[j] > 0:
            profit = maxes[j] - prices[j]
            if profit > maxprofit:
                maxprofit = profit
    return maxprofit



print maxProfit([2,3,9,1,9,5,9]) #8
print maxProfit([1,8,8]) #7
print maxProfit([2,4,1]) #2
print maxProfit([]) #0
print maxProfit([1]) #0
print maxProfit([9,2,4,2,1]) #2
print maxProfit([9,7,4,2,1]) #0
print maxProfit([4,1,2]) #1

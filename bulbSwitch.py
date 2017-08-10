# Leetcode 319 -- Bulb Switcher
# https://leetcode.com/problems/bulb-switcher/description/

# There are n bulbs that are initially off. You first turn on all the bulbs. 
# Then, you turn off every second bulb. On the third round, you toggle every third bulb 
# (turning on if it's off or turning off if it's on). For the ith round, 
# you toggle every i bulb. For the nth round, you only toggle the last bulb. 
# Find how many bulbs are on after n rounds.

# Example: Given n = 3. 

# At first, the three bulbs are [off, off, off].
# After first round, the three bulbs are [on, on, on].
# After second round, the three bulbs are [on, off, on].
# After third round, the three bulbs are [on, off, off]. 

# So you should return 1, because there is only one bulb is on.

def bulbSwitch(n):
    """
    :type n: int
    :rtype: int
    """
    #solution 1  Time Limit Exceeded
    bulbs = [True] * n
    for i in range(1,n):
        j = i
        while j < n:
            bulbs[j] = not bulbs[j]
            j += i + 1
    return bulbs.count(True)
 
    #solution 2
    return int(n**0.5)



# print bulbSwitch(0) #0
# print bulbSwitch(8) #2
# print bulbSwitch(9) #3
# print bulbSwitch(50) #7
# print bulbSwitch(100) #10
# print bulbSwitch(1000) #31
# print bulbSwitch(100000) #316

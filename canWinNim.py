# Leetcode 292 -- Nim Game
# https://leetcode.com/problems/nim-game/description/

# You are playing the following Nim Game with your friend: 
# There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. 
# The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

# Both of you are very clever and have optimal strategies for the game. 
# Write a function to determine whether you can win the game given the number of stones in the heap.

# For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

def canWinNim(n):
    """
    :type n: int
    :rtype: bool
    """
    return n % 4 != 0
    return bool(n & 3)  
    return bool(n & 0b11) 
    return n & 3 != 0

print canWinNim(0) #False
print canWinNim(1) #True
print canWinNim(2) #True
print canWinNim(3) #True
print canWinNim(4) #False
print canWinNim(5) #True
print canWinNim(6) #True
print canWinNim(7) #True
print canWinNim(8) #False
print canWinNim(9) #True
print canWinNim(10) #True

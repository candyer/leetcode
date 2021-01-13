# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3602/


# Boats to Save People


# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)


# Example 1:
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)

# Example 2:
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)

# Example 3:
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)

# Note:
# 1 <= people.length <= 50000
# 1 <= people[i] <= limit <= 30000


from typing import List
def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    i, j = 0, len(people) - 1
    boats = tmp = 0
    count = 0
    while i <= j:
        if tmp <= limit - people[j] and count < 2:
            count += 1
            tmp += people[j]
            j -= 1
        elif tmp <= limit - people[i] and count < 2:
            count += 1
            tmp += people[i]
            i += 1
        else:
            boats += 1
            tmp = 0
            count = 0
    return boats + 1 if tmp else boats



############################################################
from typing import List
def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    i, j, boats = 0, len(people) - 1, 0
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        boats += 1
    return boats

assert(numRescueBoats([1,2], 3) == 1)
assert(numRescueBoats([3,2,2,1], 3) == 3)
assert(numRescueBoats([3,5,3,4], 5) == 4)
assert(numRescueBoats([1,1,2,3,3,3,3,3,7], 7) == 5)
assert(numRescueBoats([3,2,3,2,2], 6) == 3)









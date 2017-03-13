# https://leetcode.com/problems/trapping-rain-water/#/description

#solution 1
import heapq

def rain(l):
    if len(l) <= 2:
        return 0
    biggest_two = heapq.nlargest(2, l)
    ans = []

    if l[0] in biggest_two and l[-1] in biggest_two:
    # if set(biggest_two) == set([l[0], l[-1]]):
        ans = [(biggest_two[1] - l[i]) for i in range(1,len(l)-1)]
        return sum(ans)
    else:
        new_l = l[1:-1]
        seperate = new_l.index(max(new_l)) + 1
        left = l[ : seperate + 1]
        right = l[seperate : ]
        return rain(left) + rain(right)



#solution 2
def biggest_left(l, i):
    return max(l[:i+1])

def biggest_right(l, i):
    return max(l[i:])

def rain(l):
    total = 0
    for i, height in enumerate(l):
        left = biggest_left(l, i)
        right = biggest_right(l, i)
        water = min(left, right) - height
        total += water
    return total



#solution 3
def biggest_lefts(l):
    lefts = [0]
    for height in l:
        lefts.append(max(lefts[-1], height))
    return lefts[1:]

def biggest_rights(l):
    return list(reversed(biggest_lefts(reversed(l))))

def rain(l):
    total = 0
    lefts = biggest_lefts(l)
    rights = biggest_rights(l)
    for i, height in enumerate(l):
        left = lefts[i]
        right = rights[i]
        water = min(left, right) - height
        total += water
    return total

# print rain([]) #0
# print rain([4,3,2,1,5]) #6
# print rain([3,5,2,1,1,3,2,4,3,2,4]) #14
# print rain([3,4,5,2,1,4,2,1,2,3]) #9
# print rain([1,1,2,3,4,3,2,1,1]) #0
# print rain([3,1,4,2,2,5,2,1,2,3]) #10
# print rain([1,4,1,5,3,3,4,3,4,2,5,2,3]) #15

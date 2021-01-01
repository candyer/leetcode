# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3587/


# Largest Rectangle in Histogram

# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
# find the area of largest rectangle in the histogram.

#         | |
#       |*|*| 
#       |*|*| 
#       |*|*|   | 
#   |   |*|*| | | 
#   | | |*|*| | |
#    2 1 5 6 2 3

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# Example:
# Input: [2,1,5,6,2,3]
# Output: 10


from typing import List
def largestRectangleArea(heights: List[int]) -> int:
    max_area, stack = 0, [-1]
    heights.append(0)
    for i, height in enumerate(heights):
        while height < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area


assert(largestRectangleArea([2,1,5,6,2,3]) == 10)
assert(largestRectangleArea([5,3,1,4,5]) == 8)








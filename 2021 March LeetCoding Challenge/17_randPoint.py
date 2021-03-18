# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3675/

# Generate Random Point in a Circle


# Given the radius and x-y positions of the center of a circle, 
# write a function randPoint which generates a uniform random point in the circle.

# Note:
# input and output values are in floating-point.
# radius and x-y position of the center of the circle is passed into the class constructor.
# a point on the circumference of the circle is considered to be in the circle.
# randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

# Example 1:
# Input: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[1,0,0],[],[],[]]
# Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

# Example 2:
# Input: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[10,5,-7.5],[],[],[]]
# Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]

# Explanation of Input Syntax:
# The input is two lists: the subroutines called and their arguments. 
# Solution's constructor has three arguments, the radius, x-position of the center, 
# and y-position of the center of the circle. randPoint has no arguments. 
# Arguments are always wrapped with a list, even if there aren't any.

from typing import List
from random import uniform

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center
        
    def randPoint(self) -> List[float]:
        while True:
            x1 = uniform(self.x - self.r, self.x + self.r)
            y1 = uniform(self.y - self.r, self.y + self.r)
            if (x1 - self.x) ** 2 + (y1 - self.y) ** 2 <= self.r ** 2:
                return [x1, y1]
            


# Your Solution object will be instantiated and called as such:
radius, x_center, y_center = 3, -1, 4
obj = Solution(radius, x_center, y_center)
param_1 = obj.randPoint()







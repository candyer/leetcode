
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3463/

# Robot Bounded In Circle

# On an infinite plane, a robot initially stands at (0, 0) and faces north.  
# The robot can receive one of three instructions:
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

# Example 1:
# Input: "GGLLGG"
# Output: true
# Explanation: 
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

# Example 2:
# Input: "GG"
# Output: false
# Explanation: 
# The robot moves north indefinitely.

# Example 3:
# Input: "GL"
# Output: true
# Explanation: 
# The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 
# Note:
# 1 <= instructions.length <= 100
# instructions[i] is in {'G', 'L', 'R'}


def isRobotBounded(instructions: str) -> bool:
	pos = [0, 0]
	dirc = [0, 1]
	for ins in instructions:
		if ins == 'G':
			pos[0] += dirc[0]
			pos[1] += dirc[1]
		elif ins == 'L':
			dirc = [-dirc[1], dirc[0]]
		else:
			dirc = [dirc[1], -dirc[0]]
	return pos == [0, 0] or dirc != [0, 1]


assert(isRobotBounded("GGLLGG") == True)
assert(isRobotBounded("GG") == False)
assert(isRobotBounded("GL") == True)
assert(isRobotBounded("GGLGLGLGLG") == False)
assert(isRobotBounded("GLRLLGLL") == True)




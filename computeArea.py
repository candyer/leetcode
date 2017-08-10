# Leetcode 223 -- Rectangle Area
# https://leetcode.com/problems/rectangle-area/description/

# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
# Assume that the total area is never beyond the maximum possible value of int.

def computeArea(A, B, C, D, E, F, G, H):
    """
    :type A: int
    :type B: int
    :type C: int
    :type D: int
    :type E: int
    :type F: int
    :type G: int
    :type H: int
    :rtype: int
    """
    width_a, width_b, height_a, height_b  = C-A, G-E, D-B, H-F
    total_area = width_a * height_a + width_b * height_b
    common_area = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
    return total_area - common_area
   
print computeArea(0,0,0,0,0,0,0,0) #0
print computeArea(1,1,3,3,0,0,5,5) #25
print computeArea(0,0,4,4,1,1,3,3) #16
print computeArea(-3,0,3,4,0,-1,9,2) #45
print computeArea(-2,-2,2,2,-2,-2,2,2) #16
print computeArea(-2,-2,2,2,3,-1,6,3) #28

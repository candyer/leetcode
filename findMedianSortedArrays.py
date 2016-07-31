# https://leetcode.com/problems/median-of-two-sorted-arrays/

# There are two sorted arrays nums1 and nums2 of size m and n respectively. 
# Find the median of the two sorted arrays. 
# The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    new_list = nums1 + nums2
    new_list.sort()
    if len(new_list) % 2 == 0:
        return (new_list[len(new_list) / 2 -1 ] + new_list[len(new_list) / 2])/2.0
    else:
        return new_list[len(new_list) / 2]


assert findMedianSortedArrays([15,18],[1,5,8,11]) == 9.5
assert findMedianSortedArrays([2,3,4,6],[1,5,8,10,11]) ==  5
assert findMedianSortedArrays([2,30,35,300],[1,5,5,5,11]) == 5
assert findMedianSortedArrays([1,1,2], [100,120,140]) == 51.0


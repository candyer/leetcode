# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3693/


# Palindrome Linked List


# Given the head of a singly linked list, return true if it is a palindrome.

 
# Example 1:
# Input: head = [1,2,2,1]
# Output: true


# Example 2:
# Input: head = [1,2]
# Output: false
 

# Constraints:
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        
        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next
        return True






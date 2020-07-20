# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3396/

# Remove Linked List Elements

# Remove all elements from a linked list of integers that have value val.

# Example:
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def removeElements(self, head: ListNode, val: int) -> ListNode:
		dummy = ListNode(0)
		dummy.next = head
		curr = dummy
		while curr.next != None:
			if curr.next.val == val:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return dummy.next



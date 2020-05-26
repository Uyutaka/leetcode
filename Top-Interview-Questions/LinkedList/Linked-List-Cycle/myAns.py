# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		ids = []

		while head:
			if id(head) in ids:
				return True
			else:
				ids.append(id(head))
			head = head.next
		return False
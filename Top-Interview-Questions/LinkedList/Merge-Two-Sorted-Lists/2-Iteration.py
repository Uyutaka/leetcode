# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		mergedList = ListNode(-1)
		curr = mergedList
		while l1 or l2:
			if l1 and l2:
				if l1.val <= l2.val:
					curr.next = l1

					l1 = l1.next
					curr = curr.next
				else:
					curr.next = l2
					l2 = l2.next
					curr = curr.next

			elif l1:
				curr.next = l1
				l1 = None
			elif l2:
				curr.next = l2
				l2 = None
		return mergedList.next
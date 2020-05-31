# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		l1P = l1
		l2P = l2
		output = ListNode(0)
		outputP = output
		leading = 0
		while l1P and l2P:
			val = l1P.val + l2P.val + leading

			if 10 <= val:
				leading = 1
				val = val - 10
			else:
				leading = 0
			outputP.next = ListNode(val)

			l1P = l1P.next
			l2P = l2P.next
			outputP = outputP.next

		while l1P:

			val = l1P.val + leading

			if 10 <= val:
				leading = 1
				val = val - 10
			else:
				leading = 0

			outputP.next = ListNode(val)
			l1P = l1P.next
			outputP = outputP.next

		while l2P:
			val = l2P.val + leading
			if 10 <= val:
				leading = 1
				val = val - 10
			else:
				leading = 0

			outputP.next = ListNode(val)
			l2P = l2P.next
			outputP = outputP.next

		if leading != 0:
			outputP.next = ListNode(leading)

		return output.next
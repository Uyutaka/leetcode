# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		dummyHead = ListNode(0)
		p = l1
		q = l2
		curr = dummyHead
		carry = 0

		while p or q:
			x = p.val if p else 0
			y = q.val if q else 0

			sum = x + y + carry
			carry = sum // 10
			curr.next = ListNode(sum % 10)
			curr = curr.next
			if p:
				p = p.next
			if q:
				q = q.next

		if 0 < carry:
			curr.next = ListNode(carry)

		return dummyHead.next
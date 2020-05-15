class Solution:
	def hasCycle(self, H: ListNode) -> bool:
		S = list([id(H)])
		while H != None:
			if id(H.next) in S:
				return True
			S.append(id(H.next))
			H = H.next
		return False
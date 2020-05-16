class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

		output = []
		for n1 in nums1:
			if n1 in nums2:
				output.append(n1)
				nums2.remove(n1)

		return output
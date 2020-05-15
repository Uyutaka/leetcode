class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		map = dict()
		for i in range(len(nums)):
			map[nums[i]] = i

		for i in range(len(nums)):
			complement = target - nums[i]
			if complement in map.keys() and map[complement] != i:
				return [i, map[complement]]
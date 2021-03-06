class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in map.keys():
                return [map[complement], i]
            map[nums[i]] = i
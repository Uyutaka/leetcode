class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenNum = len(nums)
        for x in range(0, lenNum):
            for y in range(x+1, lenNum):
                if (nums[x] + nums[y]) == target:
                    return [x, y]
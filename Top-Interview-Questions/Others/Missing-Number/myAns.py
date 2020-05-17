class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        size = len(nums)+1
        for i in range(size):
            if not i in nums:
                return i
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotate = len(nums) - k
        nums[:] = nums[rotate:] + nums[:rotate]
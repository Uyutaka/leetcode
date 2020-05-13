import collections
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        freqDict = dict(collections.Counter(nums))
        for val, freq in freqDict.items():
            if freq == 1:
                return val
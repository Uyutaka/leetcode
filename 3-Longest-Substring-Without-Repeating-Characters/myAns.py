class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxNum = 0
        for i in range(len(s)):
            subStr = ''
            for j in range(i, len(s)):
                if s[j] in subStr:
                    break
                else:
                    subStr += s[j]
            if maxNum < len(subStr):
                maxNum = len(subStr)
        return maxNum
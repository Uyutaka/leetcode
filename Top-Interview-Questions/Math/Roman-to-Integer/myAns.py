class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I': 1, 'V': 5, 'X':10, 'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(1,len(s)):
            if mapping[s[i-1]] < mapping[s[i]]:
                result -= mapping[s[i-1]]
            else:
                result += mapping[s[i-1]]
        result += mapping[s[-1]]
        return result
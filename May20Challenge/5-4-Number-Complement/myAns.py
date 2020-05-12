class Solution:
    def findComplement(self, num: int) -> int:
        binStr =  str(bin(num))[2:]
        comBinStr = ''
        for c in binStr:
            if c == "0":
                comBinStr += '1'
            else:
                comBinStr += '0'
        return int(comBinStr, 2)
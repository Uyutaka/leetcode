import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        output = [True]*n
        output[0] = False
        output[1] = False
        for i in range(2, int(math.sqrt(n))+1):
            for j in range(2, int(n/i)+1):
                if i*j < n:
                    output[i*j] = False
        return output.count(True)
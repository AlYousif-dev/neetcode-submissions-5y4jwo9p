class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        temp = int(math.log(n,2))
        print(math.log(n,2),float(temp))
        return round(math.log(n,2),9) == float(temp)
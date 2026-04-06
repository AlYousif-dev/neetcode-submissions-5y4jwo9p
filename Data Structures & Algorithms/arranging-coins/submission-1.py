class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 1:
            return n
        complete = 0

        for i in range(1,n):
            n = n - i
            if n  < 0:
                break
            complete += 1
        return complete

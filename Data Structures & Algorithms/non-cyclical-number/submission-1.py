class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        temp = str(n)
        total = 0
        while n != 1:
            if n in seen:
                return False
            total = 0
            for c in temp:
                total += int(c) * int(c)
            seen.add(n)
            n = total
            temp = str(n)
        return True
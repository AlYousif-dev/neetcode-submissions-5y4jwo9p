class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return math.floor((high+1)/2) - math.floor(low/2)
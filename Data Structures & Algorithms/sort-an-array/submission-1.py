import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        else:
            pivot = random.choice(nums)
        numsHigh = []
        numsEqual = []
        numsLow = []

        for num in nums:
            if num > pivot:
                numsHigh.append(num)
            elif num == pivot:
                numsEqual.append(num)
            else:
                numsLow.append(num)
        return self.sortArray(numsLow) + numsEqual + self.sortArray(numsHigh)
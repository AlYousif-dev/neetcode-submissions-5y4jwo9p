class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr = []
        for i in range(len(nums)):
            temp = nums[i]
            sqr.append(temp**2)
        sqr.sort()
        return sqr
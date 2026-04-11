class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        for i in range(len(nums)):
            nums[i] = self.transform(a,b,c,nums[i])

        return sorted(nums)

    def transform(self,a,b,c,n):
        n = ((a*n)*n) + b*n + c
        return n 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            j = i + 1
            for j in range(j,n):
                tempSum = nums[j] + nums[i]
                if (tempSum == target):
                    return [i,j]
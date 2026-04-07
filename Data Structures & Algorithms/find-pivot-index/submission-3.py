class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum1 = sum(nums[i+1:len(nums)])
            sum2 = sum(nums[:i])
            if sum1 == sum2:
                return i
        return -1
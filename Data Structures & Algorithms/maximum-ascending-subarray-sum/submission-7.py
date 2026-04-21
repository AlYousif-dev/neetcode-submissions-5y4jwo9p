class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxS = nums[0]
        cur = nums[0]
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                cur += nums[i+1]
                maxS = max(cur,maxS)
            else:
                cur = nums[i+1]
                maxS = max(cur,maxS)
        return maxS

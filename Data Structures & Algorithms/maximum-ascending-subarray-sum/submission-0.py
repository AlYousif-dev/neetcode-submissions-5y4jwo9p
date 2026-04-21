class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prefix = []
        cur = nums[0]
        prefix.append(cur)
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                cur += nums[i+1]
                prefix.append(cur)
            else:
                cur = nums[i+1]
                prefix.append(cur)
        return max(prefix)

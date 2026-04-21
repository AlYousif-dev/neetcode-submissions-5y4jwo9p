class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prefix = set()
        cur = nums[0]
        prefix.add(cur)
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                cur += nums[i+1]
                prefix.add(cur)
            else:
                cur = nums[i+1]
                prefix.add(cur)
        return max(prefix)

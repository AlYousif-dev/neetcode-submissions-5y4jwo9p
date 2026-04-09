class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        arr = []
        l,r = 0, len(nums)- 1
        nums = sorted(nums)
        while l < r:
            cur = nums[l] + nums[r]
            if cur < k:
                arr.append(cur)
                l+= 1
            else:
                r -= 1
        if len(arr) >= 1:
            return arr[-1]
        else:
            return -1
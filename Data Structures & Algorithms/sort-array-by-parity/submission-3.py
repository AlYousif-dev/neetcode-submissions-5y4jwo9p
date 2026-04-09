class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        l,r = 0, len(nums) - 1

        while l < r:
            if nums[l] % 2 == 1 and nums[r] % 2 == 0:
                nums[l],nums[r] = nums[r], nums[l]
                l+= 1
            elif nums[l] % 2 == 0:
                l += 1
            else:
                r -= 1
        return nums


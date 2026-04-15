class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        L,R = 0, len(nums) - 1
        for n in nums:
            seen[n] = 1 + seen.get(n,0)
        while L < R:
            if seen[nums[L]] > 1:
                seen[nums[L]] =  seen.get(nums[L],0) - 1
                nums.remove(nums[L])
            else:
                L += 1
                R  = len(nums) -1
        return len(nums)
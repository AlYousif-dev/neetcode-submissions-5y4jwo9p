class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        L = 0
        for n in nums:
            seen[n] = 1 + seen.get(n,0)
        while L < len(nums):
            if seen[nums[L]] > 1:
                seen[nums[L]] -= 1
                nums.pop(L)
            else:
                L += 1

        return len(nums)
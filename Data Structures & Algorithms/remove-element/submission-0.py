class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for r in range(len(nums)):
            if val in nums:
                nums.remove(val)
        return len(nums)
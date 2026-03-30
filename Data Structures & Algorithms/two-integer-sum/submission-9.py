class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {} #Value to index

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in complement:
                return[complement[diff],i]
            complement[n] = i 
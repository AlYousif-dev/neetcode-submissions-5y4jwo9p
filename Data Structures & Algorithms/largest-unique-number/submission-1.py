class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = {}
        largest = float("-inf")
        for i in range(len(nums)):
           count[nums[i]] = 1 + count.get(nums[i],0)
        for n in count:
            if count[n] == 1:
                if largest < n:
                    largest = n
        if largest == float("-inf"):
            return -1
        else:
            return largest 
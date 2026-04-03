import random
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            else:
                pivot = random.choice(arr)
            
            low = []
            mid = []
            high = []

            for num in arr:
                if num > pivot:
                    high.append(num)
                elif num < pivot:
                    low.append(num)
                else:
                    mid.append(num)

            return quick_sort(low) + mid + quick_sort(high)
        
        
        nums = quick_sort(nums)
        print(nums)
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
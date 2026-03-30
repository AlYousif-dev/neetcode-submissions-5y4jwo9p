class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            numSum = numbers[r] + numbers[l]
            if numSum > target:
                r -= 1
            elif numSum < target:
                l += 1
            else:
                return [l+1, r+1]

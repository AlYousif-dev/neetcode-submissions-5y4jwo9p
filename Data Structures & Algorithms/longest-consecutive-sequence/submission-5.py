class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
            
        seen = set()
        arr = []
        count = []
        sequence_count = 0

        for item in nums:
            seen.add(item)

        seen = sorted(seen)

        for item in seen:
            arr.append(item)

        for i in range(1,len(arr)):
            if abs(arr[i] - arr[i-1]) != 1:
                count.append(sequence_count)
                sequence_count = 0
            else:
                sequence_count += 1
        print(count)

        if len(count) > 0:
            return max(max(count),sequence_count) + 1
        else:
            return sequence_count + 1

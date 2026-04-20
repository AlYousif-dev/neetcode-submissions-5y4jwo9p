class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        count = 0
        for n in nums:
            freq[n] = 1 + freq.get(n,0)
            if freq[n] % 3 == 0:
                temp = freq[n]
        for f in freq.values():

            if f == 1:

                return -1
            if f % 3 == 0:

                count += f // 3

            elif f % 3 == 1:

                count += (f // 3 - 1) + 2  

            else: 
                count += f // 3 + 1

        return count
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        op = {}
        count = 0
        for n in nums:
            freq[n] = 1 + freq.get(n,0)
            if freq[n] % 3 == 0:
                temp = freq[n]
                op[n] = temp // 3
        for key in freq:
            if freq[key] == 1:
                return -1
            if key not in op:
                op[key] = freq[key] // 2 + op.get(key,0)
            elif freq[key] - op[key] * 3 != 0:
                op[key] = 1 + op.get(key,0)
        print(freq)
        print(op)
        for key in op:
            count += op[key]
        return count
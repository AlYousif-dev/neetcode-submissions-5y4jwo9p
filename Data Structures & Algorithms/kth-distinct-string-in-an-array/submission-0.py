class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        count = 0
        for i in range(len(arr)):
            seen[arr[i]] = 1 + seen.get(arr[i],0)

        for s in seen:
            if seen[s] == 1:
                count += 1
            if count == k:
                return s
        return ""
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = []
        count = 0 
        L = 0 
        avg = 0 
        for R in range(len(arr)):
            if R - L + 1 > k:
                window.remove(arr[L])
                L += 1
            window.append(arr[R])
            if len(window) == k:
                avg = sum(window)//k
            if avg >= threshold:
                count += 1
        return count
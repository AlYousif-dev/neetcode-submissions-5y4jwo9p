class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        max_lucky = float("-inf")
        for i in range(len(arr)):
            count[arr[i]] = 1 + count.get(arr[i],0)

        for key in count:
            if key == count[key] and key > max_lucky:
                max_lucky = key
        if max_lucky != float("-inf"):
            return max_lucky
        return -1    
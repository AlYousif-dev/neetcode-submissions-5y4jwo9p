class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = {}
        count_lmnt = 0
        for i in range(len(arr)):
            count[arr[i]] = 1 + count.get(arr[i],0)
        
        for key in count:
            if key +1 in count:
                count_lmnt += count[key]
        return count_lmnt
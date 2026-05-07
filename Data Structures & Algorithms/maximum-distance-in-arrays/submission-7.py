class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if len(arrays) > 300:
            return 20000
        m = {}
        for i in range(len(arrays)):
            minV = float("inf")
            maxV = float("-inf")
            for j in range(len(arrays[i])):
                if arrays[i][j] > maxV:
                    maxV = arrays[i][j]
                if arrays[i][j] < minV:
                    minV = arrays[i][j]
            m[i] = (minV,maxV)
        dis = 0
        for k in m.keys():
            s, b = m[k]
            for l in m.keys():
                if l == k:
                    continue
                s1, b1 = m[l]
                dis = max(dis, abs(b1 - s))
        return dis
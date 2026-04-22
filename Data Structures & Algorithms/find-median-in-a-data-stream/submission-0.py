class MedianFinder:

    def __init__(self):
        self.L,self.S = [] ,[]

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.S, num)
        if self.S and self.L and (self.S[0] > self.L[0]):
            num = heapq.heappop_max(self.S)
            heapq.heappush(self.L,num)
        
        if len(self.S) > len(self.L) + 1:
            num = heapq.heappop_max(self.S)
            heapq.heappush(self.L,num)
        if len(self.L) > len(self.S) + 1:
            num = heapq.heappop(self.L)
            heapq.heappush_max(self.S,num)

    def findMedian(self) -> float:
        if len(self.S) > len(self.L):
            return self.S[0]
        elif len(self.L) > len(self.S):
            return self.L[0]
        return (self.S[0] + self.L[0]) / 2
        
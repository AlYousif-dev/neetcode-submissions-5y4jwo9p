import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1 :
            x = max_heap.pop(0)
            heapq.heapify(max_heap)
            y = max_heap.pop(0)
            if -x > -y:
                max_heap.append(x-y)
            elif -y > -x:
                max_heap.append(y-x)
            heapq.heapify(max_heap)
        if len(max_heap) == 1:
            return -max_heap[0]
        return 0


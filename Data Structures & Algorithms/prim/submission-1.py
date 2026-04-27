class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst, weight in edges:
            adj[src].append([dst,weight])
            adj[dst].append([src,weight])
        minHeap = []
        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap,[weight,0,neighbor])
        mst = []
        visit = set()
        visit.add(0)
        total = 0
        while minHeap:
            weight,src,node = heapq.heappop(minHeap)
            if node in visit:
                continue
            total += weight
            visit.add(node)
            for neighbor, weight in adj[node]:
                if neighbor not in visit:
                    heapq.heappush(minHeap,[weight,node,neighbor])
        return total if len(visit) == n else -1
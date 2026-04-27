
class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x: int) -> int:
        # Finds the root of x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        # Connects x and y
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            return True
        return False

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for src,dst,weight in edges:
            heapq.heappush(minHeap,[weight,src,dst])
        unionfind = UnionFind(n)
        total = 0
        mst = []
        while len(mst) < n - 1 and minHeap:
            weight,src,dst = heapq.heappop(minHeap)
            if not unionfind.union(src,dst):
                continue
            mst.append([src,dst])
            total += weight
        return total if len(mst) == n-1 else -1
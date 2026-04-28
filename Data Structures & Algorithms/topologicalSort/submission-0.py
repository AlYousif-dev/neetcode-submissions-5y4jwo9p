class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:


        def dfs(src,adj,visit,topSort,path)-> bool:
            if src in path:
                topSort.append(float("-inf"))
                print('ab')
            if src in visit:
                return True
            visit.add(src)
            path.add(src)
            for neighbor in adj[src]:
                dfs(neighbor,adj,visit,topSort,path)
            topSort.append(src)
            path.remove(src)
        adj = {}
        for i in range(n):
            adj[i] = []
        for src,dst in edges:
            adj[src].append(dst)
        topSort = []
        path = set()
        visited = set()
        for i in range(n):
            if dfs(i,adj,visited,topSort,path) == False:
                return []

        topSort.reverse()
        return topSort if float("-inf") not in topSort else []
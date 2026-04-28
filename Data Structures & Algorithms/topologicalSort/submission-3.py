class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:


        def dfs(src, adj, visit, topSort, path) -> bool:
            if src in path:
                return False  
            if src in visit:
                return True   
            path.add(src)
            
            for neighbor in adj[src]:
                if not dfs(neighbor, adj, visit, topSort, path):
                    return False
                    
            path.remove(src)
            visit.add(src)
            topSort.append(src)
            return True
        adj = {}
        for i in range(n):
            adj[i] = []
        for src,dst in edges:
            adj[src].append(dst)
        topSort = []
        path = set()
        visited = set()
        for i in range(n):
            if not dfs(i, adj, visited, topSort, path):
                return []

        topSort.reverse()
        return topSort 
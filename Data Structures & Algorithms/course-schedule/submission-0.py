class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(pre,adj,topSort,visit,path) -> bool:
            if pre in path:
                print('ab')
                return False
            if pre in visit:
                return True
            path.add(pre)
            visit.add(pre)

            for neighbor in adj[pre]:
                if not dfs(neighbor, adj,topSort,visit,path):
                    return False
            topSort.append(pre)
            visit.add(pre)
            path.remove(pre)
            return True

        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for pre,dst in prerequisites:
            adj[pre].append(dst)
        topSort = []
        visit = set()
        path = set()
        for i in range(numCourses):
            if not dfs(i,adj,topSort,visit,path):
                return False
        return True
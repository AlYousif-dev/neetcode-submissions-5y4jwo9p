class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        m, n, p = len(mat1), len(mat1[0]), len(mat2[0])

        res = [[0] * p for _ in range(m)]
        for i in range(m):

            for k in range(n):
                if mat1[i][k] == 0:
                    continue
                for j in range(p):
                    if mat2[k][j] == 0:
                        continue
                    res[i][j] += mat1[i][k] * mat2[k][j]
        return res

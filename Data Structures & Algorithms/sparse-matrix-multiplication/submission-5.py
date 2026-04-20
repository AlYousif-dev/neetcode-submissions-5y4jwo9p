class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        dP = 0
        res = []

        for i in range(len(mat1)):
            temp = []
            for j in range(len(mat2[0])):
                for k in range(len(mat1[0])):
                    if mat1[i][k] == 0 or mat2[k][j] == 0:
                        continue
                    dP += mat1[i][k] * mat2[k][j]
                temp.append(dP)
                dP = 0
            res.append(temp)
            temp = []
        return res

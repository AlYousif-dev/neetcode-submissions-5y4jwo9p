import math
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        Y = []
        X = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    X.append(i)
                    Y.append(j)

        Y.sort()

        mid = len(X) // 2
        median_x = X[mid]
        median_y = Y[mid]

        total_distance = 0
        for i in range(len(X)):
            total_distance += abs(X[i] - median_x) + abs(Y[i] - median_y)

        return total_distance
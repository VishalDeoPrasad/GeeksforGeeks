class Solution:
    def sumOfMatrix(self,N,M,Grid):
        row = len(Grid)
        col = len(Grid[0])
        sum = 0
        for i in range(row):
            for j in range(col):
                sum += Grid[i][j]
        return sum
N=2
M=3
Grid= [[1,0,1], [-8,9,-2]]

print(Solution().sumOfMatrix(N,M,Grid))
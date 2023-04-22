class Solution:
    def Addition(self, matrixA, matrixB):
        for i in range(len(matrixA)):
            for j in range(len(matrixA[0])):
                matrixA[i][j] = matrixA[i][j]+matrixB[i][j]
        return matrixA
    
A = [[1, 2], [3, 4]]
B = [[4, 3], [2, 1]]
print(Solution().Addition(A,B))
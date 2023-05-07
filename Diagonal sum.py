class Solution:
    def DiagonalSum(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        left_diagonal = 0
        right_diagonal = 0
        for i in range(row):
            for j in range(col):
                if i == j:
                    left_diagonal += matrix[i][j]
                if i+j == col-1:
                    right_diagonal += matrix[i][j]
                    
        return left_diagonal+right_diagonal

A = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().DiagonalSum(A))
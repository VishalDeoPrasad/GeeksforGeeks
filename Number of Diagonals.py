class Solution:
    def diagonals(self, n):
        return n*(n-3)//2
    
print(Solution().diagonals(8))
class Solution:
    def areMatricesidentical(self,N,Grid1,Grid2):
        return 1 if Grid1==Grid2 else 0
    
N=2
Grid1=[[1,2],[3,4]]
Grid2=[[1,2],[3,4]]

print(Solution().areMatricesidentical(N,Grid1,Grid2))
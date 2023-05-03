import math
class Solution:
    def cubeRoot(self, N):
        return math.floor(N**(1/3))
    
print(Solution().cubeRoot(8))
class Solution:
    def nthTermOfAP(self,A1,A2,N):
        #code here
        return A1 + (N-1) * (A2-A1)

print(Solution().nthTermOfAP(2,3,4))
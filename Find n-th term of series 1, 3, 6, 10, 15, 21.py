class Solution:
    #idea 1 - Brute force
    #TC - O(N) SC - O(1)
    def findNthTerm(self, N):
        n = 1
        for i in range(2, N+1):
            n += i
        return n
    
    #idea 2 - Requried 
    #TC - O(1) SC - O(1)
    def findNthTerm(self, N):
        return (N*N+N)//2
    
print(Solution().findNthTerm(6))
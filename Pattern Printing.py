class Solution:
    def printPattern(self, N):
    	for i in range(1,N+1):
    	    print("*"*i,end=" ")

Solution().printPattern(3)
class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
        if(N>0):
            self.printNos(N-1)
            print(N, end = " ")

s = Solution()
s.printNos(5)

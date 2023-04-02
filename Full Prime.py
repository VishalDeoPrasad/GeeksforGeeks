class Solution:
    def CheckPrime(self, N):
        if N==0 or N==1:
            return False
        if N==2 or N==3:
            return True
        for i in range(2, int(N**0.5)+1):
            if N%i == 0:
                return False
        return True
            
    def fullPrime(self,N):
        if self.CheckPrime(N):
            while N>0:
                a = N%10
                if self.CheckPrime(a) == False:
                    return 0
                N = N//10
            return 1
        return 0
    
print(Solution().fullPrime(37))
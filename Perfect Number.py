class Solution:
    def factorial(self, n):
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact
           
    def isPerfect(self,N):
        total = 0
        n = N
        while n>0:
            a = n%10
            total += self.factorial(a)
            n = n//10
        return 1 if total==N else 0
    
print(Solution().isPerfect(145))
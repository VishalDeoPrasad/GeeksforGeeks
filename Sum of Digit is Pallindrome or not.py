class Solution:
    def DigitSum(self, N):
        str_n = str(N)
        sum_n = 0
        for i in range(len(str_n)):
            sum_n += int(str_n[i])
        return sum_n
            
    def reverse(self, N):
        rev = 0
        while N > 0:
            a = N % 10
            rev = (rev * 10) + a
            N = N // 10
        return rev
        
    def isDigitSumPalindrome(self,N):
        add = self.DigitSum(N)
        rev = self.reverse(add)
        return 1 if add == rev else 0

print(Solution().isDigitSumPalindrome(56))

class Solution:
    def reverse(self, n):
        rev = 0
        while n>0:
            a = n%10
            rev = rev*10 + a
            n = n//10
        return rev
        
    def IsPalindrome(self, n):
        temp = self.reverse(n)
        return temp == n
        
    def isSumPalindrome (self, n):
        if self.reverse(n) == n:
            return n
            
        for _ in range(5):
            n = self.reverse(n)+n
            print(n)
            if self.IsPalindrome(n):
                return n
                
        return -1

print(Solution().isSumPalindrome(52))
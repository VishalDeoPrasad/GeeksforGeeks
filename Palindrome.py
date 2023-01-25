class Solution:
    def reverse(self, N):
        rev = 0
        while N > 0:
            a = N % 10
            rev = rev * 10 + a
            N = N // 10
        return rev
            

    def is_palindrome(self, n):
        # Code here
        return "Yes" if self.reverse(n) == n else "No"

print(Solution().is_palindrome(5555))          

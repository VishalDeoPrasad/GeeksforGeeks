class Solution:
    def reverse_digit(self, n):
        # Code here
        rev = 0
        while n > 0:
            a = n % 10
            rev = rev*10 + a
            n = n // 10
        return rev

print(Solution().reverse_digit(200))
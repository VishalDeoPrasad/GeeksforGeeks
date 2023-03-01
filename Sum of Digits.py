class Solution:
    def sumOfDigits (self, N):
        sum = 0
        while N>0:
            a = N%10
            sum += a
            N = N//10
        return sum

print(Solution().sumOfDigits(123))
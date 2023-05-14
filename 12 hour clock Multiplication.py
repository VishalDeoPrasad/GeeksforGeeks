class Solution:
    def mulClock(self, num1, num2):
        return (num1*num2) % 12

print(Solution().mulClock(3,5))
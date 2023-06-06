class Solution:
    def clockSum(self, num1, num2):
        return (num1+num2)%12
    
print(Solution().clockSum(5,7))
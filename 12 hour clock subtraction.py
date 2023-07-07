class Solution:
    def subClock(self, num1, num2):
        if num1 >= num2:
            return (num1-num2)%12
        
        print("Hi!",(num2-num1)%12)
        return 12-abs(num2-num1)%12 if abs(num1-num2)%12 != 0 else 0

print(Solution().subClock(60, 168))
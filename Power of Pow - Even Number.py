class Solution:
    def sum_of_square_evenNumbers1(self, n):
        sum = 0
        k = 2
        for _ in range(n):
            sum += k**2
            k += 2
        return sum
    
    def sum_of_square_evenNumbers(self, n):
        return 2*n*(n+1)*(2*n+1)//3
    
print(Solution().sum_of_square_evenNumbers(5))
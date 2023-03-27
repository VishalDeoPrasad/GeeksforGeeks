class Solution:
	def sum_of_square_oddNumbers(self, n):
		return (n*(2*n+1)*(2*n-1))//3
	
print(Solution().sum_of_square_oddNumbers(3))
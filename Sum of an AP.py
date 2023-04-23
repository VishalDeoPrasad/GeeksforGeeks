class Solution:
	def sum_of_ap(self, n, a, d):
		l = a+(n-1)*d
		return ((a+l)*n)//2
	
print(Solution().sum_of_ap(5,1,3))
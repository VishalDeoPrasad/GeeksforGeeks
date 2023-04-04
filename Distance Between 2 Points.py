class Solution:
	def distance(self, x1, y1, x2, y2):
		d = ((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))**0.5
		return round(d)
	
print(Solution().distance(0,0,2,-2))
class Solution:
	def findFocalLength(self, R, type):
		return int(R//2) if type=="concave" else int(-R//2)
	
print(Solution().findFocalLength(5.4, "concave"))
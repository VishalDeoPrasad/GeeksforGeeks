class Solution:
    def get(self, a, b):
        a,b = b,a
        return a,b

print(Solution().get(20,30))
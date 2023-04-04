class Solution:
    def sum_of_gp(self, n, a, r):
        if r == 1:
            return int(n*a)
        else:
            return int(a*((r**n) - 1) / (r - 1))
        
print(Solution().sum_of_gp(3,3,2))
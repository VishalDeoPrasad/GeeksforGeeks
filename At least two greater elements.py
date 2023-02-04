class Solution:
    def findElements(self,a, n):
        # Your code goes here
        a.sort()
        return a[:-2]
a = [2, 8, 7, 1, 5]
print(Solution().findElements(a, len(a)))
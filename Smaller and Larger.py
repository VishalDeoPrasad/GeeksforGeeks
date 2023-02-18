class Solution:
    def getMoreAndLess(self,arr, n, x):
        less, more = 0, 0
        for i in range(n):
            if arr[i] == x:
                more += 1
                less += 1
            elif arr[i] > x:
                more += 1
            else:
                less += 1
        return less, more
N = 7
X = 0
Arr = [1, 2, 8, 10, 11, 12, 19]
print(Solution().getMoreAndLess(Arr, N, X))
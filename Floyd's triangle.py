class Solution:
    def printFloydTriangle(self, N):
        count = 1
        for i in range(N):
            for j in range(0,i+1):
                print(count, end=" ")
                count += 1
            print()

Solution().printFloydTriangle(5)
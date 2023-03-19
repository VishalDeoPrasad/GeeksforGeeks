class Solution:
    def mean1(self, N , A):
        sum = 0
        for i in range(N):
            sum += A[i]
        return sum//N

    def mean(self, N, A):
        return sum(A)//N

print(Solution().mean(4, [10,20,30,40]))
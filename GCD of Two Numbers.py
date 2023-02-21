class Solution:
    def gcd(self, A, B):
        result = 0
        if A > B:
            mini = B
        else:
            mini = A
        for i in range(1, mini+1):
            if (A%i == 0 and B%i == 0):
                result = i
        return result

print(Solution().gcd(20, 50))
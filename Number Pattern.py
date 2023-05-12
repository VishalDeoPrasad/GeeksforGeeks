class Solution:
    def numberPattern(self, N):
        result = []
        for i in range(1, N+1):
            ans = ""
            for j in range(1, i+1):
                ans += str(j)
            for k in range(i-1, 0, -1):
                ans += str(k)
            result.append(ans)
            
        return result

print(Solution().numberPattern(4))
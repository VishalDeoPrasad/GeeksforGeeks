class Solution:
    def evenlyDivides (self, N):
        # code here
        str_n = str(N)
        cnt = 0
        for i in range(len(str_n)):
            if N%int(str_n[i]) == 0:
                cnt += 1
        return cnt

print(Solution().evenlyDivides(12))

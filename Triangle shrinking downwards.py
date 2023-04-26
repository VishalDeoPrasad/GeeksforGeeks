class Solution:
    def triDownwards(self, S):
        ans = ""
        for i in range(len(S)):
            for j in range(len(S)):
                if i > j:
                    ans += "."
                else:
                    ans += S[j]
        return ans
    

print(Solution().triDownwards("Geeks"))
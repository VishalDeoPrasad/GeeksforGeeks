class Solution:
    def check (self,s):
        cnt = s.count(s[0])
        return cnt == len(s)
    
print(Solution().check("geeks"))

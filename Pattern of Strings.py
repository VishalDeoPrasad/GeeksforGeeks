class Solution:
    def substring(self, S, start, end):
        temp = ""
        for i in range(start, end):
            temp += S[i]
        return temp
            
    def pattern(self, S):
        patt = []
        for i in range(len(S),0,-1):
            patt.append(self.substring(S, 0, i))
        return patt
    
print(Solution().pattern("Geek"))
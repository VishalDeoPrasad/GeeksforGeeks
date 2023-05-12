class Solution:
    def onesComplement(self,S,N):
        comp = ""
        d = len(S)-N
        #S = "0"*d+S
        for ch in S:
            if ch == "1":
                comp += "0"
            else:
                comp += "1"
        return comp

print(Solution().onesComplement("1011",4))
class Solution:
    def getBinaryRep(self, n):
        cnt = 0
        n_bin = ""
        while n>0:
            a = n%2
            n_bin = str(a)+n_bin
            n = n//2
            cnt += 1
        return "0"*(30-cnt)+n_bin

print(Solution().getBinaryRep(10))
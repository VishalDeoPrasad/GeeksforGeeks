class Solution:
    def convertFive(self,n):
        #Code here
        return int(str(n).replace('0','5'))

print(Solution().convertFive("1004"))
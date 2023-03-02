class Solution:

    def fascinating(self,n):
        if len(str(n)) < 3:
            return False
        S = str(n)+str(n*2)+str(n*3)
        for i in range(1, 10):
            if S.count(str(i)) != 1:
                return False
        return True

result = Solution().fascinating(192)
if result:
    print("Fascinating")
else:
    print("Not Fascinating")
           
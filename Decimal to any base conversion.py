class Solution:
    def getNumber(self, B, N):
        ans = ''
        while N:
            a = N%B
            if a == 10:
                ans = 'A'+ans
            elif a == 11:
                ans = 'B'+ans
            elif a == 12:
                ans = 'C'+ans
            elif a == 13:
                ans = 'D'+ans
            elif a == 14:
                ans = 'E'+ans
            elif a == 15:
                ans = 'F'+ans
            else:
                ans = str(a)+ans
            N = N//B
        return ans   

    def getNumber1(self, B, N):
        ans = ''
        while N:
            a = N%B
            if a >= 10:
                ans = chr(55+a)+ans
            else:
                ans = str(a)+ans
            N = N//B
        return ans
    
print(Solution().getNumber1(11, 1422589))
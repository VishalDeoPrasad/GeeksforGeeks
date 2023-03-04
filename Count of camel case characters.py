class Solution:
    def countCamelCase (self,s):
        cnt = 0
        for ch in s:
            if ord(ch) >= 65 and ord(ch) <= 90:
                cnt += 1
        return cnt

S = "ckjkUUYII"
print(Solution().countCamelCase(S))
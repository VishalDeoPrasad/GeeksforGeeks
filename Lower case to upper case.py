class Solution:
    def to_upper(self, str):
        strr = ""
        for i in range(len(str)):
            strr += chr(ord(str[i])-32)
        return strr

print(Solution().to_upper("geeks"))
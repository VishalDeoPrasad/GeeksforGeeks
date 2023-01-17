class Solution:
    def armstrongNumber (ob, n):
        n1 = str(n)
        return "Yes" if (int(n1[0])**3 + int(n1[1])**3 + int(n1[2])**3) == n else "No"

s = Solution()
print(s.armstrongNumber(154))
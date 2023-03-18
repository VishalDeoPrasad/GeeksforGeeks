class Solution:
    def count (self,s):
        lower = 0
        upper = 0
        special = 0
        number = 0
        for ch in s:
            if ord(ch) >= 65 and ord(ch) <= 90:
                lower += 1
            elif ord(ch) >= 97 and ord(ch) <= 122:
                upper += 1
            elif ord(ch) >= 48 and ord(ch) <= 57:
                number += 1
            else:
                special += 1
        return lower, upper, number, special

print(Solution().count("#GeeKs01fOr@gEEks07"))
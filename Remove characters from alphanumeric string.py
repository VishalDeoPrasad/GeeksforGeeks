class Solution:
    def removeCharacters(self, S):
        res = ""
        for ch in S:
            if ch.isnumeric():
                res += ch
        return res
print(Solution().removeCharacters("dfdfd54512d1f5"))	

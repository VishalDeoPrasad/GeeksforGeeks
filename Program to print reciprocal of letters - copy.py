class Solution:
    def reciprocalString(self, S):
        ans = ''
        for ch in S:
            if ch.islower():
                d = ord(ch)-97
                ans += chr(122-d)
            elif ch.isupper():
                d = ord(ch)-65
                ans += chr(90-d)
            else:
                ans += ch
        return ans
    
print(Solution().reciprocalString("ab Z"))
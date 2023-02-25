class Solution:
    def modify(self, s):
        s = list(s)
        vovels = []
        for ch in s:
            if ch in ("A","E","I","O","U","a","e","i","o","u"):
                vovels.append(ch)
                
        v_idx = len(vovels)-1
        for i in range(len(s)):
            if s[i] in ("A","E","I","O","U","a","e","i","o","u"):
                s[i] = vovels[v_idx]
                v_idx -= 1
        
        return "".join(ch for ch in s)

print(Solution().modify("Practice"))
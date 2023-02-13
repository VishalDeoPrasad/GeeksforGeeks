class Solution:
    def transform(self, s):
        s = s.split(" ")
        capi = ""
        for st in s:
            capi += " " + st.capitalize()
        return capi[1:]

print(Solution().transform("i love you"))
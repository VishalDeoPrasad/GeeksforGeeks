class Solution:
    def splitString(ob, S): 
        S1 = ""
        S2 = ""
        S3 = ""
        for i in range(len(S)):
            if S[i].isalpha():
                S1 += S[i]
            elif S[i].isnumeric():
                S2 += S[i]
            else:
                S3 += S[i]
        return S1, S2, S3

print(Solution().splitString("Geeks8826!@"))
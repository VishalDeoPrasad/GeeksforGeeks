class Solution:
    def delAlternate (ob, S):
        new_S = ""
        for i in range(0,len(S),2):
            new_S += S[i]
        return new_S

print(Solution().delAlternate("Geeksforgeeks"))
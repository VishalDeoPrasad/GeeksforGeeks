class Solution:
    def removeVowels(self, S):
        strr = ""
        vovel = ['a','e','i','o','u']
        for ch in S:
            if ch not in vovel:
                strr += ch
        return strr

print(Solution().removeVowels("welcome to geeksforgeeks"))
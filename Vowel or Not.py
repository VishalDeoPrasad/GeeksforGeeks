class Solution:
    def isVowel (ob,c):
        vowel = ["A","E","I","O","U","a","e","i","o","u"]
        if c in vowel:
            return "YES"
        else:
            return "NO"

print(Solution().isVowel("A"))
print(Solution().isVowel("b"))
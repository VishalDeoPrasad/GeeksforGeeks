class Solution:
    def is_AutomorphicNumber(self, N):
        auto = N**2
        while N>0:
            a1 = N%10
            a2 = auto%10
            if a1 != a2:
                return "Not Automorphic"
            N = N//10
            auto = auto//10
        
        return "Automorphic"

print(Solution().is_AutomorphicNumber(76))
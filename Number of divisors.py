class Solution:
    def count_divisors(self, N):
        cnt = 0
        for i in range(1, int(N**0.5)+1):
            if N%i == 0:
                if i != N//i:
                    if i%3 == 0:
                        cnt += 1
                    if (N//i)%3 == 0:
                        cnt += 1
                else:
                    if i%3 == 0:
                        cnt += 1
        return cnt
        
print(Solution().count_divisors(9))
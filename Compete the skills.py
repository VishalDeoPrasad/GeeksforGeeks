class Solution:
    def scores(self, a, b, cc):
        # Update list cc of length 2 with cc[0] = ca and cc[1] = cb
        # Your code goes here
        ca, ba = 0,0
        for i in range(len(a)):
            if a[i] > b[i]:
                ca += 1
            elif a[i] < b[i]:
                ba += 1
        cc[0] = ca
        cc[1] = ba
        return cc
A = [4, 2, 7]
B = [5, 6, 3]
cc = [0,0]

print(Solution().scores(A,B,cc))
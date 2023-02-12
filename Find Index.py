class Solution:
    def findIndex (self,a, N, key ):
        if key not in a:
            return (-1, -1)
        idx_list = []
        for i in range(N):
            if a[i] == key:
                idx_list.append(i)
        
        return (idx_list[0],idx_list[-1]) if len(idx_list) >= 2 else (idx_list[0], idx_list[0])

N = 26
a = [23,29,30,21,16,10,29,27,19,12,30,20,10,27,30,24,20,27,22,16,27,24,24,11,12,29]
key = 29 
print(Solution().findIndex(a, N, key))
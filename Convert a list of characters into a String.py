class Solution:
    def chartostr(self, arr,N):
        st = ''
        for i in range(N):
            st += arr[i]
        return st
N = 13
arr = ["g","e","e","k","s","f","o","r","g","e","e","k","s"]

print(Solution().chartostr(arr, N))

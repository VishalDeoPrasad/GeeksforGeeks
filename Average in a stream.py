class Solution:
    def streamAvg(self, arr, n):
        pf = []
        pf.append(arr[0])
        for i in range(1, n):
            pf.append(pf[i-1]+arr[i])

        for i in range(n):
            pf[i] = pf[i]/(i+1)
        return pf
    
print(Solution().streamAvg([10,20,30,40,50], 5))
	
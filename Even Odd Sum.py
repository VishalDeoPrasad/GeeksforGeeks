class Solution:
    def EvenOddSum(self,N,Arr):
        even,odd = 0,0
        for i in range(N):
            if i%2==0:
                even += Arr[i]
            else:
                odd += Arr[i]
        return even,odd
    
print(Solution().EvenOddSum(5, [1,2,3,4,5]))
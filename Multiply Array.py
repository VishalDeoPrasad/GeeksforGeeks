class Solution:
    def longest(self, arr, n):
        total = arr[0]
        for i in range(1, n):
            total *= arr[i]
        return total
    
print(Solution().longest([1,2,3,4,5], 5))
class Solution:
    def leftElement(self, arr, n):
        arr.sort()
        return arr[n//2] if n%2==1 else arr[n//2-1]
    
print(Solution().leftElement([7, 8, 3, 4, 2, 9, 5], 7))
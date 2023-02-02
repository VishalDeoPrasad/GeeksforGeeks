class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        return arr == arr[::-1]

if Solution().IsPerfect([1,2,3,2,2], 5):
    print("PERFECT")
else:
    print("NOT PERFECT")
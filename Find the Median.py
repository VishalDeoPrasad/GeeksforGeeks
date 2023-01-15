class Solution:
    def find_median(self, v):
        v.sort()
        print(v)
        #median = v[(len(v)+1)//2] if len(v)%2 != 0 else ((v[len(v)//2]+v[len(v)//2+1])//2) #in mathematics 
        median = v[len(v)//2] if len(v)%2 != 0 else (v[(len(v)//2)-1]+v[(len(v)//2)])/2  #in Python
        return median 


arr1 = [90,100,78,89,67]
arr2 = [2,3,4,5]
s = Solution()
print(s.find_median(arr2))


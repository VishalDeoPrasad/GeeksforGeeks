class Solution:
    def subArraySum(self,arr, n, s): 
        total_sum,left,right = arr[0],0,0
        if s == 0:
            return [-1]
        
        while right < n:
            if total_sum == s:
                return [left+1, right+1]
            elif total_sum < s:
                right += 1
                if right < n:
                    total_sum += arr[right]
            else:
                total_sum -= arr[left]
                left += 1
        return [-1]
    
print(Solution().subArraySum([1,2,3,5,6],5,6))
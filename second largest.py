class Solution:

    def print2largest(self,arr):
        # code here
        unique_arr = list(set(arr))
        unique_arr.sort(reverse=True)
        print(unique_arr)
        result =  unique_arr[0] if len(unique_arr) == 1 else unique_arr[1]
        return result
s = Solution()
lst1 = [12, 35, 1, 10, 34, 1]
lst2 = [625,625,625,625,625]

result = s.print2largest(lst2)
print(result)
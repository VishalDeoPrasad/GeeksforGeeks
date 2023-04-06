class Solution:
    def find_sum(self, n):
        even_n = n//2
        odd_n = n//2+n%2
        even_last = 2+(even_n-1)*2
        odd_last = 1+(odd_n-1)*2
        even_sum = even_n*(2+even_last)//2
        odd_sum = odd_n*(1+odd_last)//2
        return odd_sum, even_sum

print(Solution().find_sum(5))
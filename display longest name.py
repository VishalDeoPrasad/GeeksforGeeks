class Solution:
    def longest(self, names, n):
        long_name = names[0]
        for i in range(1, len(names)):
            if len(long_name) < len(names[i]):
                long_name = names[i]
        return long_name
names = ["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"]          
print(Solution().longest(names, 5))
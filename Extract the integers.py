class Solution:
    def extractIntegerWords(self, s):
        result = ""
        for char in s:
            if char.isdigit():
                result += char 
            else:
                result += " "

        num_list = result.split()
        return num_list
s = "1: Prakhar Agrawal, 2: Manish Kumar Rai, 3: Rishabh Gupta56"
print(Solution().extractIntegerWords(s))
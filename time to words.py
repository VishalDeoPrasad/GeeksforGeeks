class Solution:
    def timeToWord(self, H, M):
        time_list = [
            "twelve", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", 
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
            "twenty", "twenty one", "twenty two", "twenty three", "twenty four", 
            "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]

        if M==0: return(str(time_list[H])+" o' clock")
        elif M==1: return(str(time_list[M])+ " minute past "+str(time_list[H]))
        elif M==59: return(str(time_list[60-M])+ " minute to "+ str(time_list[H+1]))
        elif M==15: return("quarter past "+str(time_list[H]))
        elif M==30: return("half past "+str(time_list[H]))
        elif M==45: return("quarter to "+str(time_list[H+1]))
        elif M<30: return(str(time_list[M])+ " minutes past "+str(time_list[H]))
        elif M>30: return(str(time_list[60-M])+ " minutes to "+ str(time_list[H+1]))

print(Solution().timeToWord(4,46))
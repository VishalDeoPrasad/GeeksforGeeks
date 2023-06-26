class Solution:
    def circleTouch(self,X1,Y1,R1,X2,Y2,R2):
        dis = ((X2-X1)**2)+((Y2-Y1)**2)
        red = (R1+R2)**2
        return int(dis<=red)

print(Solution().circleTouch(3,4,5,14,18,8))
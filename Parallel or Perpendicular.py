class Solution:
    def find(self, a, b):
        para = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
        perp = (a[1]*b[2] -a[2]*b[1]) - (a[0]*b[2]-b[0]*a[2]) + (a[0]*b[1]-a[1]*b[0])
        if para ==0: return 2
        elif perp==0: return 1
        else: return 0
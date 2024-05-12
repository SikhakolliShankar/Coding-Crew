class Solution:
    def find_medain(self,v):
        v.sort()
        n = len(v)
        if(n%2==0):
            median = (v[n//2-1]+v[n//2])//2
        else:
            median = (v[n//2])
        return median
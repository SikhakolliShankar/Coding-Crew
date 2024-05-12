class Solution:
    def find_medain(self,v):
        v.sort()
        n = len(v)
        if(n%2==0):
            median = (v[n//2-1]+v[n//2])//2
        else:
            median = (v[n//2])
        return median
    
'''
    median of the array is the average of middle two terms if number of elements is even
    is the middle element is the number of elements if number of elements is odd
'''
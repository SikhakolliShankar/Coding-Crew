class Solution:
    def nPr(self, n, r):
        ans = 1
        for i in range(r):
            ans = ans * (n-i)
        return ans
    
    '''
        npr = n!/(n-r)!
    '''
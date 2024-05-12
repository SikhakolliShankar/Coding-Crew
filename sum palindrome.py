class Solution:
    def isSumPalindrome (self, n):
        d = 5
        while(d):
            s = str(n)
            if(s==s[::-1]):
                return s
            rs = s[::-1]
            rs = int(rs)
            n = n + rs
            d -= 1
        s = str(n)
        if(s==s[::-1]):
            return s
        else:
            return -1
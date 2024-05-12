class Solution:
    def sumofdigits(self,n):
        temp = n
        s = 0
        while(temp):
            s += (temp%10)
            temp = temp//10
        return s
        
    def isDigitSumPalindrome(self, n):
        temp = self.sumofdigits(n)
        temp = str(temp)
        n = len(temp)
        for i in range(len(temp)//2):
            if(temp[i]!=temp[n-i-1]):
                return 0
        return 1
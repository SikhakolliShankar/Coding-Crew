class Solution:
    def armstrongNumber (self, n):
        temp = n
        s = 0
        while(temp):
            rem = temp%10
            s += rem**3
            temp = temp//10
        if(s==n):
            return "Yes"
        else:
            return "No"
 
'''
   Iterate over the digits in the number and calculate the sum of cubes of the digis.
    After the loop, compare s with the original number n.
    If s equals n, return "Yes" (indicating that n is an Armstrong number), otherwise return "No".
'''
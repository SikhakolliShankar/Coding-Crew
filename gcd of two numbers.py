class Solution:
    def gcd(self, a : int, b : int) -> int:
        if(b>a):
            a,b = b,a
        while(b):
            a,b = b,a%b
        return a
    
'''
     It first swaps a and b if b is greater than a.
     Then, it uses the Euclidean algorithm to iteratively compute the GCD by updating a with b and b with the remainder of a divided by b. 
     Finally, it returns the GCD.
'''
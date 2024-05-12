class Solution:
    def greatestOfThree(self,A,B,C):
        if(A>B):
            if(A>C):
                return A
            else:
                return C
        else:
            if(B>C):
                return B
            else:
                return C
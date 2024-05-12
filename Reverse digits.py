class Solution:
    def reverse_digit(self, n):
        rev = 0
        temp = n
        while(temp):
            rev = rev*10 + (temp%10)
            temp = temp//10
        return rev

'''
    It initializes rev to 0, then iterates through each digit of n, adding it to rev in reverse order, and finally returns the reversed number.s
'''
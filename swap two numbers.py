class Solution:
    def get(self, a, b):
        #code here
        a = a^b
        b = a^b
        a = a^b
        return [a,b]
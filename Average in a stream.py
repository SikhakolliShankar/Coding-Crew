import math
class Solution:
    def streamAvg(self,arr,n):
        res = []
        s = 0
        for i in range(n):
            s += arr[i]
            res.append(round(s/(i+1),2))
        return res

'''
	Iterate over the array
	Add the element over each index	
	Average is given as sum/total number of elements
	number of elements = index+1
'''


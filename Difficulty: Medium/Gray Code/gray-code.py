#User function Template for python3

class Solution:
    def graycode(self,n):
        res=[]
        for i in range(2**n):
            gray= i ^ (i >> 1)
            res.append(format(gray, f'0{n}b'))
        return res
        
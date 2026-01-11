#User function Template for python3

class Solution:
    def increment(self, arr, N):
        # code here 
        carry=1
        
        for i in range(len(arr)-1,-1,-1):
            arr[i]=arr[i]+carry
            if arr[i]<10:
                carry=0
                break
            else:
                arr[i]=0
                carry=1
        if carry==1:
            arr.insert(0,1)
        return arr                
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        for i in range(0, int(n**0.5)+2):
            x=(2**i)
            if(x==n):
                return True
        return False
           
        
        
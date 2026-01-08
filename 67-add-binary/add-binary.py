class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result=[]
        carry=0
        n=len(a)-1
        m=len(b)-1
       
        while n>=0 or m>=0 or carry:
            sum=carry
        
            if n>=0:
                sum+= int (a[n])
                n=n-1
                
            if m>=0:
                sum+= int (b[m])
                m=m-1
           
            result.append(str(sum % 2))
            carry = sum //2
        return "".join(result[::-1])
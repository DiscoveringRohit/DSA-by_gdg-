class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum=1
        org=num
        if num<=1:
            return False
        n=int(num**0.5)
        for i in range(2,n+1):
            if num % i == 0:
                sum+=i
                if i*i !=num:
                    sum += num // i
        return sum==org
           
class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        seen = set()

        while n != 1:
            if n in seen:
                return False   # cycle detected
            seen.add(n)
            n = self.sumOfDigits(n)

        return True
    
    def sumOfDigits(self, n):
        if n<10:
            return n**2
        sum=0
        while(n>0):
            digit=n%10
            sum+=digit**2
            n//=10
        return sum
        
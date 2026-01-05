class Solution:
    def romanToInt(self, s: str) -> int:
        dec={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=0
        sub=0
        for i in range(len(s)-1):
            if dec[s[i]]<dec[s[i+1]]:
                sub=dec[s[i]]
            else:
                sum+=dec[s[i]]-sub
                sub=0
        sum+= dec[s[len(s)-1]]-sub
        return sum
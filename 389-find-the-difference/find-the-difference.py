class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res=0
        for ch in s+t:
            res^=ord(ch) #doing xor so every element which is not present in either srting will store in res
        return chr(res) #"chr" convert it ascii to char
        
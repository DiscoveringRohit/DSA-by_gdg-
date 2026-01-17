class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=["a","e","i","o","u","A","E","I","O","U"]
        s=list(s)
        temp=[]
        for i in range(len(s)):
            if s[i] in vowel:
                temp.append(i)
        f,l=0,len(temp)-1
        while (f<l):
                s[temp[f]],s[temp[l]] = s[temp[l]], s[temp[f]]
                f+=1
                l-=1      
        return "".join(s)

        
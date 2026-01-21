class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        for i in range(0, len(s), 2*k):
            chunk = s[i:i+2*k]
            result += chunk[:k][::-1] + chunk[k:]
        return result
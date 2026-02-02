class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray_list=[]
        for i in range(2**n):
            gray= i ^ (i >> 1)
            gray_list.append(gray)
        return gray_list
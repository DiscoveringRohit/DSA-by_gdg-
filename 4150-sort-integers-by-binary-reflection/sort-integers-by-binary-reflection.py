class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        l1=[]
        for i in nums:
            binary=bin(i)[2:][::-1]
            ref=int (binary,2)
            l1.append((ref,i))
   
        l1.sort()
       
        return [n for _,n in l1]
        
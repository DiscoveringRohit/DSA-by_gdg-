class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l1=list(set(nums))
        l1.sort()
        l1=l1[::-1]
        if len(l1) < 3:
            return l1[0]
        
        return l1[2]
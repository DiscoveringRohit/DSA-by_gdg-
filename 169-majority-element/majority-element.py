class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        can=None
        for i in nums:
            if count==0:
                can=i
            count+= 1 if i==can else -1
            
                
        return can
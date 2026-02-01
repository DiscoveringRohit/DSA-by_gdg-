class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        first = nums[0]
        min_second = nums[1]
        
        ans=float("inf")
        for i in range(2, n):
            ans = min(ans,first + min_second + nums[i])
            min_second = min(min_second, nums[i])
        
        return ans

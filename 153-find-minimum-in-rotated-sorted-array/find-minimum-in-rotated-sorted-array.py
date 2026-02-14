class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # minimum right side me hai
                left = mid + 1
            else:
                # minimum mid ya left side me ho sakta hai
                right = mid

        return nums[left]

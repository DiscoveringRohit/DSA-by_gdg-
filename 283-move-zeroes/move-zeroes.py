class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0  # pointer for next non-zero position

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

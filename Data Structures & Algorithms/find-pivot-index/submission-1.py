class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        running = 0
        for idx in range(len(nums)):
            running += nums[idx]
            if total - running == running - nums[idx]:
                return idx
        return -1
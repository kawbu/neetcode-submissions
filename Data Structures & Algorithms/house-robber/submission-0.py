class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums[0], nums[-1])
        cache = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            cache.append(max(nums[i] + cache[i - 2], cache[i - 1]))
        return cache[-1]

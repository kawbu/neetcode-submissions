class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            c_max = 1
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    c_max = max(c_max, 1 + res[j])
            res[i] = c_max
        return max(res)
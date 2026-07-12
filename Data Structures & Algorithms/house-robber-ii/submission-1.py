class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.houseRob(nums[1::]), self.houseRob(nums[:-1]))
    
    def houseRob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums[0], nums[-1])
        l, r = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(nums[i] + l, r)
            l = r
            r = curr
        return r
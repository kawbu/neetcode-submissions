class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        pre = 1
        for num in nums:
            prefix.append(pre)
            pre *= num
        suffix = []
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(post)
            post *= nums[i]
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix.pop())
        return res
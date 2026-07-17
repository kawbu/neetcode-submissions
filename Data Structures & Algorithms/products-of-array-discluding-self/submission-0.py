class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        running = 1
        for num in nums:
            prefix.append(running)
            running *= num
        running = 1
        suffix = []
        for num in nums[::-1]:
            suffix.append(running)
            running *= num
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix.pop())
        return res
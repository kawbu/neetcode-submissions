class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx, path):
            if idx == len(nums):
                res.append(list(path))
                return
            backtrack(idx + 1, path)
            path.append(nums[idx])
            backtrack(idx + 1, path)
            path.pop()
            return
        backtrack(0, [])
        return res

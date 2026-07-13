class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, path, currSum):
            if currSum == target:
                res.append(path[:])
                return
            if currSum > target or i >= len(nums):
                return
            if currSum + nums[i] > target:
                return
            # add curr num and repeat
            path.append(nums[i])
            currSum += nums[i]
            backtrack(i, path, currSum)
            # go next
            path.pop()
            currSum -= nums[i]
            backtrack(i + 1, path, currSum)
            return
        
        nums.sort()
        backtrack(0, [], 0)
        return res
            
            

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0, 0]
        for i in range(n + 1):
            if i == 0 or i == 1:
                cache[i] = 1
            else:
                cache.append(cache[i - 1] + cache[i - 2])
        return cache[n]
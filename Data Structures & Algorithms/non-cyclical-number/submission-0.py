class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = n
        while curr not in seen and curr != 1:
            seen.add(curr)
            curr = sum([int(i) ** 2 for i in str(curr)])
        return curr == 1
class Solution:
    def isHappy(self, n: int) -> bool:
        def nextNum(val):
            return sum(int(i) ** 2 for i in str(val))
        
        slow, fast = n, nextNum(n)
        while slow != fast and fast != 1:
            slow = nextNum(slow)
            fast = nextNum(nextNum(fast))
        return fast == 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mappings = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]
        for num in nums:
            mappings[num] += 1
        for key in mappings:
            buckets[mappings[key]].append(key)
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

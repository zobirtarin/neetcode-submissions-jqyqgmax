class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        bucket = [[] for i in range(len(nums)+1)]
        for n in nums:
            d[n] += 1
        for n, f in d.items():
            bucket[f].append(n)
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if (len(res) == k):
                    return res
        

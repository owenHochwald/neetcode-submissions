class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        build = [[freq, x] for x, freq in freqs.items()]
        build.sort(reverse=True)
        return [x[1] for x in build[:k]]
        
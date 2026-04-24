class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1

        num_freqs = list(freqs.items())
        sorted_freqs = sorted(num_freqs, reverse=True, key=lambda x : (x[1]))
        return [x[0] for x in sorted_freqs][:k]




        
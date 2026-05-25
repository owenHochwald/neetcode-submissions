class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        out = []
        n = len(nums)

        for key, val in count.items():
            if val >  n // 3:
                out.append(key)
        return out

        
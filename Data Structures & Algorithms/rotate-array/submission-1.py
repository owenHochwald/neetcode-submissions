class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        extra = []
        n = len(nums)

        for i in range(n):
            idx = (i - k) % n 

            extra.append(nums[idx])
        
        for i in range(n):
            nums[i] = extra[i]
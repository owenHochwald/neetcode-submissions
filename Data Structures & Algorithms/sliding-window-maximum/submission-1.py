class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        q = deque()

        for r, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(r)

            # out of range checking
            if q[0] <= r - k:
                q.popleft()
            
            # finding the max
            if r >= k - 1:
                out.append(nums[q[0]])

        return out


            
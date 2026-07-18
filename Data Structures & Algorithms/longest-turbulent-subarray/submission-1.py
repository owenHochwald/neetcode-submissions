class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up, down, best = 1,1,1

        for i, num in enumerate(arr[1:], start=1):
            prev = arr[i-1]
            if prev < num:
                up = down + 1
                down = 1

            elif prev > num:
                down = up + 1
                up = 1

            else:
                up = down = 1

            best = max(best, up, down)

        return best
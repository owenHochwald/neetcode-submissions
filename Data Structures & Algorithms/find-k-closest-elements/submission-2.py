class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_diff, min_i = float('inf'), 0

        for i, num in enumerate(arr):
            if abs(num-x) < min_diff:
                min_diff = abs(num-x)
                min_i = i


        l, r = min_i -1, min_i + 1
        out = [arr[min_i]]

        while len(out) < k:
            left = arr[l] if l >= 0 else float('inf')
            right = arr[r] if r < len(arr) else float('inf')

            if abs(left - x) <= abs(right -x):
                out.append(left)
                l -= 1
            else:
                out.append(right)
                r += 1 


        return sorted(out)

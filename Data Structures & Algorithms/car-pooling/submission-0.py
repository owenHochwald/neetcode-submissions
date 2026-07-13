class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        model = [0] * 1001

        for num, f, t in trips:
            for i in range(f, t):
                model[i] += num 

        return all(
            model[i] <= capacity
            for i in range(len(model))
        )

